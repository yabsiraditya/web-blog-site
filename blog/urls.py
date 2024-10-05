from django.urls import path

from . import views

# app_name = Blog
urlpatterns = [
    path('', views.index),
    path('detail/<slug:slugInput>/', views.detail_artikel),
    path('kategori/<slug:kategoriInput>/', views.detail_kategori),
]