from django.shortcuts import render
from django.http import HttpResponse

def user_profile_view(request):
    return HttpResponse("<h2>مرحباً بك في تطبيق الحسابات والمستخدمين (Account App) 👤</h2>")