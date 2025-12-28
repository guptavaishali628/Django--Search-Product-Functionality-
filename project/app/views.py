from django.shortcuts import render, redirect
from .models import AddCardData

# Create your views here.
def home(req):
    return render(req,'home.html')

def add_card(req):
    return render(req, 'add_card.html')

def add_item(req):
    
    if req.method=="POST":
        name=req.POST.get('name')
        price=req.POST.get('price')
        company=req.POST.get('company')
        image=req.FILES.get('image')

        AddCardData.objects.create(Name=name, Price=price, Company=company, Image=image)

        return redirect('home') 


def show_item(req):
    pass