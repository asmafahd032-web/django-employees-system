from django.shortcuts import render
import datetime

def home(request):
    #تنفيذ المحاضرة
   # context = {
      #  "course_name": "asma"
    #}
    # 1. المتغيرات المحلية الخاصه بنظام الموظفين
    context = {
        "employee_name": "asma fahd",
        "job_title": "software engineer",
        "salary": 12500.50,
        "bonus": 500,
        "bio": "experienced python and django developer",
        "employees_list": ["Asma", "sma", "Mohammed", "Ahmed"],
        "join_date": datetime.date(2026, 7, 21),
        "is_active": True,
        "skills_count": 0, # سنستخدم هذا لشرط القيمة الفارغة أو الصفرية
    }
    return render(request, "employees/index.html", context)

def about(request):
    return render(request, "employees/about.html")