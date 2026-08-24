from django.urls import path
from . import views
app_name = "account"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
      path('register/', views.register_view, name='register'),  #  رابط تسجيل حساب جديد
      path('queryset-demo/', views.queryset_demo, name='queryset_demo'),
     path('profile/add/', views.add_user_profile, name='add_user_profile'),
path('profile/success/', views.profile_success, name='profile_success'),

       
]



