from django.shortcuts import render, redirect

from .models import Slider, Quote


# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    quotes = Quote.objects.all()
    return render(request, 'home.html', {'sliders': sliders, 'quotes': quotes})

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def view(request):
    return render(request, 'view.html')







