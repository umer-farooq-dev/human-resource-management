from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from human_resource_management import settings
from hrm_admin import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.login, name="login"),
                  path('home/', views.home, name="home"),
                  path('newsfeed/', views.NewsFeed, name="newsfeed"),
                  path('onedrive/', views.Onedrive, name="onedrive"),
                  path('organization/', views.Organization, name="organization"),
                  path('business/', views.BusinessStrategy, name="business"),
                  path('human-resource/', views.human_resources, name="human-resource"),
                  path('tech-service/', views.tech_service, name="tech-service"),
                  path('ethics-security/', views.ethics_security, name="ethics-security"),
                  path('leadership/', views.leadership, name="leadership"),
                  path('employee-login/', views.employee_login, name="employee-login"),
                  path('employee-dashboard/', views.employees_dashboard, name="employee-dashboard"),
                  path('all-employee/', views.all_employees, name="all-employee"),
                  path('employee-list/', views.employees_list, name="employee-list"),
                  path('employee-profile/', views.employee_profile, name="employee-profile"),
                  path('employee-holidays/', views.employee_holidays, name="employee-holidays"),
                  path('employee-leave/', views.employee_leave, name="employee-leave"),
                  path('employee-attendance/', views.employee_attendance, name="employee-attendance"),
                  path('clint/', views.clint, name="clint"),
                  path('timesheet/', views.timesheet, name="timesheet"),
                  path('rough/', views.rough, name="rough"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
