from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Categories, Products
from .forms import CategoriesForm, ProductsForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def home(request):
    categories = Categories.objects.all()
    products = Products.objects.all()
    return render(request, 'index.html', {"navbar":"home", "categories":categories, "products":products})

def about(request):
    return render(request, 'about.html', {"navbar":"about"})

def blog(request):
    return render(request, 'blog.html', {"navbar":"blog"})


def gallery(request):
    categories = Categories.objects.all()
    products = Products.objects.all()
    return render(request, 'gallery.html', {"navbar":"gallery", "categories":categories, "products":products})


def contact(request):
    return render(request, 'contact.html', {"navbar":"contact"})

def categories(request, name):
    try:
        category = Categories.objects.get(name = name)
        cat_products = Products.objects.filter(category = category)
        return render(request, 'category.html', {'cat_products':cat_products, 'category':category})
    except:
        messages.warning(request, "That category doesn't exist")
    return redirect('/')

def create_categories(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CategoriesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/")
    else:
        form = CategoriesForm()
    return render(request, 'create_categories.html', {"navbar":"create categories", 'form': form})

def create_products(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProductsForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/")
    else:
        form = ProductsForm()
    return render(request, 'create_products.html', {"navbar":"create products", 'form': form})