
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.


def index(request):
    products = Product.objects.all()
    # print(products)
    # print(products.product_id)
    n = len(products)
    no_of_slides = n//4+ceil(n/4 - n//4)

    # params={'products':products,'no_of_slides':no_of_slides,'range':range(1,no_of_slides)}
    # alproduct = [[products, no_of_slides, range(1, no_of_slides)], [products, no_of_slides, range(1, no_of_slides)], [
    #     products, no_of_slides, range(1, no_of_slides)], [products, no_of_slides, range(1, no_of_slides)]] # this total code is for teh creating the multiple slides on the webiste.Now we are creating the real category website.
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        no_of_slides = n//4+ceil(n/4 - n//4)
        allprods.append([prod,no_of_slides,range(1,no_of_slides)])
    params = {'alproduct': allprods}
    # return HttpResponse("Helllo , Customers.")
    return render(request, 'shop/index.html', params)


def Contact(request):
    return HttpResponse("this is the Contact us form of our website.")


def search(request):
    return HttpResponse("this is the search us form of our website.")


def productview(request):
    return HttpResponse("this is the productview us form of our website.")


def checkout(request):
    return HttpResponse("this is the checkout us form of our website.")


def Aboutus(request):
    # return HttpResponse("this is the Aboutus us form of our website.")
    return render(request, 'shop/about.html')


def tracker(request):
    return HttpResponse("this is the trac")
