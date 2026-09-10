from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile, Skill



from django.core.mail import send_mail
from .forms import UserProfileForm, TeacherEmailForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        user_input = request.POST.get('username_or_email')
        password_input = request.POST.get('password')
        user = authenticate(
            request,
            username=user_input,
            password=password_input
        )

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(
                request,
                'اسم المستخدم أو كلمة المرور غير صحيحة'
            )

    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('account:login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')

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
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            login(
                request,
                user,
                backend='django.contrib.auth.backends.ModelBackend'
            )
            messages.success(
                request,
                'تم إنشاء الحساب وتسجيل الدخول بنجاح!'
            )
            return redirect('/')

    return render(request, 'account/register.html')


@login_required
def queryset_demo(request):
    # 1. all(): جلب جميع الموظفين
    all_employees = UserProfile.objects.all()

    # 2. filter(): جلب الموظفين النشطين
    active_employees = UserProfile.objects.filter(is_active=True)

    # 3. exclude(): استبعاد المديرين
    non_admin_employees = UserProfile.objects.exclude(role='admin')

    # 4. get(): جلب الموظف أحمد
    ahmed = UserProfile.objects.get(username='ahmed')

    # 5. order_by(): ترتيب الموظفين حسب الاسم
    ordered_employees = UserProfile.objects.order_by('full_name')

    # 6. count(): حساب عدد الموظفين والمهارات
    employee_count = UserProfile.objects.all().count()
    skill_count = Skill.objects.all().count()

    # 7. exists(): التحقق من وجود أحمد
    ahmed_exists = UserProfile.objects.filter(username='ahmed').exists()

    context = {
        'all_employees': all_employees,
        'active_employees': active_employees,
        'non_admin_employees': non_admin_employees,
        'ahmed': ahmed,
        'ordered_employees': ordered_employees,
        'employee_count': employee_count,
        'skill_count': skill_count,
        'ahmed_exists': ahmed_exists,
    }

    return render(request, 'account/queryset_demo.html', context)

@login_required
def add_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('account:profile_success')
    else:
        form = UserProfileForm()

    return render(request, 'account/user_profile_form.html', {'form': form})


def profile_success(request):
    return render(request, 'account/profile_success.html')


@login_required
def send_teacher_email(request):
    if request.method == 'POST':
        form = TeacherEmailForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email=None,
                recipient_list=['engreemalwaeel@gmail.com'],
                fail_silently=False,
            )
            return redirect('account:email_success')
    else:
        form = TeacherEmailForm()

    return render(
        request,
        'account/teacher_email.html',
        {'form': form}
    )


@login_required
def email_success(request):
    return render(request, 'account/email_success.html')
