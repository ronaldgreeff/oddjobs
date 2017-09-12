# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Listing

def index(request):
	listings = Listing.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'listings/index.html', {'listings': listings})

def listing_detail(request, pk):
	listing = get_object_or_404(listing, pk=pk)
	return render(request, 'listings/listing_detail.html', {'listing': listing})
"""
was:
def Listing_detail(request, pk):
	Listing.objects.get(pk=pk)
"""