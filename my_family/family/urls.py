from django.urls import path

from family import views

app_name = 'family'
urlpatterns = [
    path('familiar', views.familiar, name='family-list')
]
