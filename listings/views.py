# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Listing, Trade
from .forms import ListingForm, TradeForm

def index(request):
	listings = Listing.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'listings/index.html', {'listings': listings})

def listing_new(request):
	if request.method == "POST":
		form = ListingForm(request.POST)
		if form.is_valid():
			listing = form.save(commit=False)
			listing.listee = request.user
			listing.created_date = timezone.now()
			listing.create()
			return redirect('listing_detail', pk=listing.pk)
	else:
		form = ListingForm()
		return render(request, 'listings/listing_edit.html', {'form': form})

def listing_detail(request, pk):
	listing = get_object_or_404(Listing, pk=pk)
	return render(request, 'listings/listing_detail.html', {'listing': listing},)

"""def listing_offer(request, pk):
	if request.method == "POST":
		form = TradeForm():
"""
"""Model Reference:
Listing:
	is_assigned = models.BooleanField(default=False)
	listee = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	listing_dscr = models.TextField(max_length=500)
	created_date = models.DateTimeField(blank=True, null=True)
	assigned_date = models.DateTimeField(blank=True, null=True)
	completed_date = models.DateTimeField(blank=True, null=True)
"""

def listing_edit(request, pk):
	listing = get_object_or_404(Listing, pk=pk)
	if request.method == "POST":
		form = ListingForm(request.POST, instance=listing)
		if form.is_valid():
			listing = form.save(commit=False)
			listing.listee = request.user
			listing.created_date = timezone.now()
			listing.save() #changed to listing.save, works!
			return redirect('listing_detail', pk=listing.pk)
	else:
		form = ListingForm(instance=listing)
	return render(request, 'listings/listing_edit.html', {'form': form})

#working on below
def listing_offer(request, pk):
	listing = get_object_or_404(Listing, pk=pk)
	if request.method == "POST":
		form = TradeForm(request.POST, instance=listing),
		if form.is_valid():
			listing = form.save(commit=False)
			listing.listee = request.user
			listing.created_date = timezone.now()
			listing.save() #changed to listing.save, works!
			return redirect('listing_detail', pk=listing.pk)
	else:
		form = TradeForm(instance=listing)
	return render(request, 'listings/listing_offer.html', {'form': form})
"""
Trade:
	trader = models.ForeignKey('auth.User')
	listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
	amount_listed = Listing.amount_listed
	amount_offered = models.DecimalField(max_digits=6, decimal_places=2)
	amount_accepted = models.DecimalField(max_digits=6, decimal_places=2)
	
	trade_choices = models.CharField
"""