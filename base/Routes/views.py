from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def hero_landing(request):
    return render(request, 'hero-landing.html')

