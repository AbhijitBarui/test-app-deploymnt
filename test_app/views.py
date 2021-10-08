from django.shortcuts import render

def index(request):
    return render(request, 'test_app/index.html')

def about(request):
    return render(request, 'test_app/about.html')