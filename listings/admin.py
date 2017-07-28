# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Listing
from .models import Trade

admin.site.register(Listing)
admin.site.register(Trade)
# Register your models here.