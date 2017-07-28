# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Listing

def index(request):
	listings = Listing.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'listings/index.html', {'listings': listings})