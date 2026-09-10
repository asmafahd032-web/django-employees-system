#يظهر النموذج داخل لوحه الاداره 
from django.contrib import admin
from .models import Product

admin.site.register(Product)