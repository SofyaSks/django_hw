from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mainpage'),
    path('register/', views.register, name='register'),
    path('login/', views.loginme, name='login'),
]