from django.shortcuts import render
from django.utils import timezone

from .models import Listing

from search.documents import ListingDocument


def search(request):
    q = request.GET.get('q')
    if q:
        p = ListingDocument.search().query("match", journaltitle=q)
        listings = p.to_queryset()
    else:
        listings = Listing.objects.filter(added_date__lte=timezone.now()).order_by('added_date')

    return render(request, 'predatoryjournals/predatoryjournals.html', {'listings': listings})
