# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^listing/(?P<pk>\d+)/$', views.listing_detail, name='listing_detail'),
]
# Create your urls here.