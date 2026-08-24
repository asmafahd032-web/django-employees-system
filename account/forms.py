#from django import forms
#from .models import Transaction
from django import forms
from .models import UserProfile, Skill

# نموذج إضافة وتعديل بيئة الموظف (ModelForm)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'username', 'email', 'phone', 'role', 'is_active', 'skills']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الكامل'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المستخدم'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهاتف'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'skills': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
        }

    # التحقق من صحة البيانات (Validation Customization)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com') and not email.endswith('@company.com'):
            raise forms.ValidationError("يرجى إدخال بريد إلكتروني رسمي ينتهي بـ @gmail.com أو @company.com")
        return email
