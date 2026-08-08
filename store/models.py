from django.db import models

class Product(models.Model):
    # حقول بيانات المنتجات
    name = models.CharField(max_length=150, verbose_name="اسم المنتج/الخدمة")
    category = models.CharField(max_length=50, verbose_name="نوع المنتج أو القسم")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    stock_quantity = models.IntegerField(default=0, verbose_name="الكمية المتوفرة")
    is_available = models.BooleanField(default=True, verbose_name="متوفر للبيع")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    def __str__(self):
        return f"{self.name} - ({self.price} $)"