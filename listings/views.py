# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Listing
from .forms import ListingForm

def index(request):
	listings = Listing.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'listings/index.html', {'listings': listings})

def listing_detail(request, pk):
	listing = get_object_or_404(Listing, pk=pk)
	return render(request, 'listings/listing_detail.html', {'listing': listing})

def listing_new(request):
	if request.method == "POST":
		form = ListingForm(request.POST)
		if form.is_valid():
			listing = form.save(commit=False)
			listing.listee = request.user
			listing.created_date = timezone.now()
			listing.save()
			return redirect('listing_detail', pk=listing.pk)
	else:
		form = ListingForm()
		return render(request, 'listings/listing_edit.html', {'form': form})