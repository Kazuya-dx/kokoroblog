from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('tag/<pk>', views.tag_blog, name='tag_blog'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('test/', views.test, name='test'),
]
