from django.shortcuts import render

def home(request):
    return render(request, "employees/index.html")

def about(request):
    return render(request, "employees/about.html")
# Create your views here.
