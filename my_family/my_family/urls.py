"""my_family URL Configuration

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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from my_family.views import hello_world
from family.views import create_familiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('create_familiar/<str:name>/<str:last_name>/<int:numberphone>/<str:due_date>/', create_familiar),
    path('family/', include('family.urls')),
]
