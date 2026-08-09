from django.shortcuts import render
import datetime

def home(request):
    context = {
        "employee_name": "asma fahd",
        "job_title": "Software Engineer",
        "salary": 1500,
        "bonus": 500,
        "bio": "experienced python and django developer",
        "employees_list": ["Asma", "Sma", "Mohammed", "Ahmed"],
        "join_date": datetime.date(2026, 7, 21),
        "is_active": True,
        "skills_count": 0,
    }
    return render(request, "employees/index.html", context)

def about(request):
    return render(request, "employees/about.html")