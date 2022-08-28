from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from human_resource_management import settings
from hrm_admin import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.login, name="login"),
                  path('home/', views.home, name="home"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
