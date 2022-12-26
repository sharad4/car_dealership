from django.shortcuts import render
from .models import Listings
from .forms import ListingForm

# Create your views here.
def listings(request):
    listings = Listings.objects.all()
    context = {
        'listings':listings
    }

    return render(request, 'listings.html', context)

def listing(request, id):
    listing = Listings.objects.get(id=id)
    context = {
        'listing':listing,
    }
    return render(request,'listing.html', context)

def create(request):
    form = ListingForm()
    context = {
        'form':form
    }
    return render(request,'create.html', context)
