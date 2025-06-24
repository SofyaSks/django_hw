from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_article, name='new_article'),
    path('<int:uid>/', views.article, name='article'),
    path('myfetch/', views.myfetch, name='myfetch'),
    path('table/', views.multTable, name='table'),
    path('', views.all_blog_posts, name='feed'),
    path('last_posts/', views.new_blog_posts),
    path('update/<int:article_id>/', views.update_article, name='update_article')

    ]