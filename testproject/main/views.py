from django.shortcuts import render

def index(request):
    return render(request, 'mainn/index.html')

def about(request):
    return render(request, 'mainn/about.html')
