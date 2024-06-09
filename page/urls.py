# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.jadval, name='index'),
    path('add_person/', views.add_person, name='add_person'),
    path('success/', views.success, name='success'),
]
