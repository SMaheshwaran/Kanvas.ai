from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def hero_landing(request):
    return render(request, 'hero-landing.html')

