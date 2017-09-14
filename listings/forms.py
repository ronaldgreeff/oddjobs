from django import forms

from .models import Listing

#ListingForm = name of form
class ListingForm(forms.ModelForm):

	class Meta:
		model = Listing
		fields = ('title','listing_dscr',)

"""
Model Reference:

class Listing(models.Model):
	is_assigned = models.BooleanField(default=False)
	listee = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	listing_dscr = models.TextField(max_length=500)

	created_date = models.DateTimeField(blank=True, null=True)
	assigned_date = models.DateTimeField(blank=True, null=True)
	completed_date = models.DateTimeField(blank=True, null=True)

	def create(self):
		self.created_date = timezone.now()
		self.save()

	def amount_listed(self):
		self.amount_listed = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return self.title
"""