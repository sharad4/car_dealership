from django.forms import ModelForm
from .models import Listings

class ListingForm(ModelForm):
    class Meta:
        model = Listings
        fields = [ 
            'name',
            'description',
            'brand',
            'milage',
            'price',
            'image'
        ]