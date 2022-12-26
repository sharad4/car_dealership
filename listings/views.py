from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = ListingForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {
        'form':form
    }
    return render(request,'create.html', context)

def update(request,id):
    listing = Listings.objects.get(id=id)
    form = ListingForm(instance = listing)
    if request.method == "POST":
        form = ListingForm(request.POST,instance = listing, files=request.FILES)
        if form.is_valid:
            form.save()
        return redirect('/')
    context = { 
        'form':form
    }
    return render(request,'update.html',context)

def delete(request,id):
    listing = Listings.objects.get(id=id)
    listing.delete()
    return redirect('/')
