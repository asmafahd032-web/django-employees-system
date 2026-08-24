#from django.contrib import admin
#from .models import UserProfile

#admin.site.register(UserProfile)
from django.contrib import admin
from .models import UserProfile, Skill, Transaction

# تخصيص عرض المهارات/المشاريع
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# تخصيص عرض ملف الموظف والعلاقات
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'email', 'role', 'is_active', 'created_at')
    list_filter = ('role', 'is_active')
    search_fields = ('full_name', 'username', 'email')
    # الواجهة الخاصة بعلاقة Many-to-Many لاختيار المهارات بسهولة
    filter_horizontal = ('skills',)

# تخصيص عرض المعاملات المالية
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'amount', 'transaction_type', 'date')
    list_filter = ('transaction_type', 'date')
    search_fields = ('user_profile__full_name', 'transaction_type')