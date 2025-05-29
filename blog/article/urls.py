from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_article, name='new_article'),
    path('<int:uid>/', views.article, name='article'),
    ]