
# Create your models here.
from django.db import models

class UserProfile(models.Model):
    # خيارات أدوار المستخدمين في النظام
    ROLE_CHOICES = [
        ('admin', 'مدير النظام'),
        ('manager', 'مدير قسم'),
        ('employee', 'موظف'),
    ]

    # حقول البيانات التي سنحفظها لكل مستخدم
    full_name = models.CharField(max_length=100, verbose_name="الاسم الكامل")
    username = models.CharField(max_length=50, unique=True, verbose_name="اسم المستخدم")
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="رقم الهاتف")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee', verbose_name="الصلاحية/الدور")
    is_active = models.BooleanField(default=True, verbose_name="حساب نشط")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ إنشاء الحساب")

    def __str__(self):
        return f"{self.full_name} - {self.get_role_display()}"