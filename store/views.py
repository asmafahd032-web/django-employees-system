from django.shortcuts import render
from django.http import HttpResponse

def product_list_view(request):
    return HttpResponse("<h2>مرحباً بك في قائمة منتجات ونظام الشركة 📦</h2>")