from django.shortcuts import render
from search.documents import PostDocument

#Deubg
from elasticsearch_dsl import Q


def search(request):
    q = request.GET.get('q')
    if q:
        #p = PostDocument.search().query("match", title=q)
        qy = Q("multi_match", query=q, fields=['title', 'text'])
        s = PostDocument.search()
        p = s.query(qy)
        posts = p.to_queryset()
        t = [_.to_dict(include_meta=False) for _ in p]
    else:
        posts = ''
        t = ''

    return render(request, 'search/search.html', {'posts': posts, 'ps': t})
