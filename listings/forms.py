from django.forms import ModelForm

from . models import Listing, Trade

class ListingForm(ModelForm):
	class Meta:
		model = Listing
		fields = ('title', 'listing_dscr', 'amount_listed',)

class TradeForm(ModelForm):
	class Meta:
		model = Trade
# in the example, collingrady.wp, he excludes the foreign.key containing model attribute, in our case being:
		exclude = ('listing',)
"""Model Reference:
Listing:
	is_assigned = models.BooleanField(default=False)
	listee = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	listing_dscr = models.TextField(max_length=500)
	created_date = models.DateTimeField(blank=True, null=True)
	assigned_date = models.DateTimeField(blank=True, null=True)
	completed_date = models.DateTimeField(blank=True, null=True)
Trade:
	trader = models.ForeignKey('auth.User')
	listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
	amount_listed = Listing.amount_listed
	amount_offered = models.DecimalField(max_digits=6, decimal_places=2)
	amount_accepted = models.DecimalField(max_digits=6, decimal_places=2)
	
	trade_choices = models.CharField"""