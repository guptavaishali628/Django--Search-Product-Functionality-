from django.shortcuts import render, redirect
from .models import AddCardData

# Create your views here.

def home(req):
    Add_Card_data=AddCardData.objects.all()
    return render(req,'home.html',{'data':Add_Card_data})

def add_card(req):
    return render(req, 'add_card.html')

def add_item(req):
    # storing data in database
    if req.method=="POST":
        name=req.POST.get('name')
        price=req.POST.get('price')
        company=req.POST.get('company')
        image=req.FILES.get('image')

        AddCardData.objects.create(Name=name, Price=price, Company=company, Image=image)

        return redirect('home') 


def search(req):
    # searching item
    if req.method=='POST':
        search=req.POST.get('search')

        if search:
            Alldata=AddCardData.objects.filter(Name__contains=search) # here we use col__contains --> lookup field
            Alldata=AddCardData.objects.filter(Company__contains=search)
            return render(req,'home.html',{'data':Alldata})
        else:
            Alldata=AddCardData.objects.all()    
        
        return render(req,'home.html',{'Alldata':Alldata})

def low_to_high(req):
    Alldata=AddCardData.objects.order_by('Price') 
    return render(req,'home.html',{'data':Alldata})

def high_to_low(req):
    Alldata=AddCardData.objects.order_by('-Price')
    return render(req,'home.html',{'data':Alldata})

def arrange_by_name(req):
   Alldata=AddCardData.objects.order_by('Name') 
   return render(req,'home.html',{'data':Alldata})

def price_between(req):
    Alldata=AddCardData.objects.filter(Price__lte=500) # here we use col__lte --> lookup field
    return render(req,'home.html',{'data':Alldata})


def price_above(req):
    Alldata=AddCardData.objects.filter(Price__gt=500) # here we use col__ --> lookup field
    return render(req,'home.html',{'data':Alldata})

def show_item(req):
    pass
             
        
        