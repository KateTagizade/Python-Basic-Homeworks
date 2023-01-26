"""growinghappy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from services.views import main_page
from services.views import ServiceListView
from services.views import ServiceDetailView
from services.views import ServiceCreateView


urlpatterns = [
    path('', main_page),
    path('admin/', admin.site.urls),
    path('services', ServiceListView.as_view(), name ='services'),
    path('services/<int:pk>', ServiceDetailView.as_view(), name='service'),
    path('services/create/', ServiceCreateView.as_view(), name='service_create'),
]
