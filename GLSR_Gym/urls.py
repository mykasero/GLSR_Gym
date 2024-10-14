"""
URL configuration for GLSR_Gym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Schedule.admin import admin_site

from django.templatetags.static import static
from django.views.generic.base import RedirectView


admin_site._registry.update(admin.site._registry)
urlpatterns = [
    path('', include('Schedule.urls')),
    path('admin/', admin_site.urls),
    path('', include("django.contrib.auth.urls")),
    path('favicon.ico', RedirectView.as_view(url=static('favicon.ico'))),
]
