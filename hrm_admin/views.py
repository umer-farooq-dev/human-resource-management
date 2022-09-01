from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def BusinessStrategy(request):
    return render(request=request, template_name="business.html")


def home(request):
    return render(request=request, template_name="home.html")


def login(request):
    return render(request=request, template_name="login.html")


def NewsFeed(request):
    return render(request=request, template_name="newsfeed.html")


def Onedrive(request):
    return render(request=request, template_name="onedrive.html")


def Organization(request):
    return render(request=request, template_name="organization.html")


def human_resources(request):
    return render(request=request, template_name="human_resources.html")


def tech_service(request):
    return render(request=request, template_name="tech_service.html")


def ethics_security(request):
    return render(request=request, template_name="ethics_security.html")


def leadership(request):
    return render(request=request, template_name="leadership.html")


def employees_dashboard(request):
    return render(request=request, template_name="Employee/dashboard.html")


def all_employees(request):
    return render(request=request, template_name="Employee/all_employees.html")


def employees_list(request):
    return render(request=request, template_name="Employee/employee_list.html")


def employee_profile(request):
    return render(request=request, template_name="Employee/employee_profile.html")


def employee_holidays(request):
    return render(request=request, template_name="Employee/holidays.html")


def employee_leave(request):
    return render(request=request, template_name="Employee/employee_leaves.html")


def employee_login(request):
    return render(request=request, template_name="Employee/login.html")


def employee_attendance(request):
    return render(request=request, template_name="Employee/employee_attendance.html")


def clint(request):
    return render(request=request, template_name="Employee/clint.html")


def timesheet(request):
    return render(request=request, template_name="Employee/timesheet.html")

