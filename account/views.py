from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('username_or_email')
        password_input = request.POST.get('password')

        user = authenticate(request, username=user_input, password=password_input)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'اسم المستخدم / البريد الإلكتروني أو كلمة المرور غير صحيحة')

    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('account:login')
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'كلمات المرور غير متطابقة!')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'اسم المستخدم مستخدم بالفعل!')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'البريد الإلكتروني مستخدم بالفعل!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            # تم تحديد backend هنا ليعرف جانغو طريقة الدخول
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'تم إنشاء الحساب وتسجيل الدخول بنجاح!')
            return redirect('/')

    return render(request, 'account/register.html')