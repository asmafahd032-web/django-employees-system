from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='اسم المهارة'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='الوصف'
    )

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('employee', 'موظف'),
        ('admin', 'مدير'),
    )

    # علاقة واحد إلى واحد مع مستخدم Django
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='المستخدم المرتبط',
        null=True,
        blank=True
    )

    full_name = models.CharField(
        max_length=100,
        verbose_name='الاسم الكامل'
    )
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='اسم المستخدم'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='البريد الإلكتروني'
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='رقم الهاتف'
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='employee',
        verbose_name='الدور'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='حساب نشط'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ إنشاء الحساب'
    )

    # علاقة كثير إلى كثير مع المهارات
    skills = models.ManyToManyField(
        Skill,
        blank=True,       #السماح بإنشاء ملف موظف دون اختيار مهارة
        related_name='employees',#الوصول إلى الموظفين الذين يمتلكون المهارة
        verbose_name='المهارات'
    )

    def __str__(self):
        return self.full_name


class Transaction(models.Model):
    # علاقة كثير إلى واحد مع UserProfile
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name='الموظف',
        null=True,
        blank=True
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name='المبلغ'
    )
    transaction_type = models.CharField(
        max_length=50,
        default='راتب',
        verbose_name='نوع المعاملة'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='التاريخ'
    )

    def __str__(self):
        if self.user_profile:
            return f'{self.user_profile.full_name} - {self.amount}'
        return f'معاملة - {self.amount}'
