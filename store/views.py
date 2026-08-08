from django.shortcuts import render
from .models import Product  # جلب كلاس المنتجات

def product_list_view(request):
    # 1. جلب كل المنتجات المخزنة من قاعدة البيانات
    products_list = Product.objects.all()

    # 2. إرسال المنتجات إلى صفحة الـ HTML
    context = {
        'products': products_list
    }
    return render(request, 'store/products.html', context)