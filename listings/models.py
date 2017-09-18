# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Listing(models.Model):
	is_assigned = models.BooleanField(default=False)
	listee = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	listing_dscr = models.TextField(max_length=500)
	amount_listed = models.DecimalField(max_digits=6, decimal_places=2)
	created_date = models.DateTimeField(blank=True, null=True)
	assigned_date = models.DateTimeField(blank=True, null=True)
	completed_date = models.DateTimeField(blank=True, null=True)

	def create(self):
		self.created_date = timezone.now()
		self.save() 

	def __str__(self):
		return self.title

class Trade(models.Model):
	trader = models.ForeignKey('auth.User')
	listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
	amount_offered = models.DecimalField(max_digits=6, decimal_places=2)
	amount_accepted = models.DecimalField(max_digits=6, decimal_places=2)
	
	ACCEPT = 'AC'
	WAIT = 'WT'
	DECLINE = 'DC'
	WITHDRAW = 'WD'
	TRADE_CHOICES = (
		('AC', 'Accept'),
		('WT', 'Wait'),
		('DC', 'Decline'),
		('WD', 'Withdraw'),
	)
	trade_choices = models.CharField(
		max_length=2,
		choices=TRADE_CHOICES,
		default=ACCEPT,
	)

	def offered(self):
		self.offered = amount_offered
		self.assigned_date = timezone.now()
		self.save()

	def assigned(self):
		self.accepted = amount_accepted
		self.assigned_date = timezone.now()
		self.save()

	def done(self):
		self.completed_date = timezone.now()
		self.save()
"""
	listing_id = models.ForeignKey(User, on_delete=models.CASCADE)
	location = 
	starred = 

class Jobs(models.Model):
	job_id = models.ForeignKey(Listing, on_delete=models.CASCADE)

class Payment(models.Model):
	do_for = (more,less)
	accepted = models.DateTimeField('date accepted')

class User(models.Model):
	jobs_posted = 
	jobs_posted_live = 
	jobs_won = 
	jobs_done = 
"""
# Create your models here.