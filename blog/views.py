from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import PostForm
from .models import Post
from search.documents import PostDocument

# For custom querying
from elasticsearch_dsl import Q
#from elasticsearch_dsl import Search
#from elasticsearch import Elasticsearch


def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # return render(request, 'blog/post_list.html', {'posts': posts})
    q = request.GET.get('q')
    meta_info = {}

    if q:
        qy = Q("multi_match", query=q, fields=['title', 'text'])
        s = PostDocument.search()
        p = s.query(qy)
        posts = p.to_queryset()
        meta_info['results_count'] = len(posts)
        meta_info['query'] = q
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts, 'meta_info': meta_info})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})