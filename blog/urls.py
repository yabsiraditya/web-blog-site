from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('kategori/<slug:kategoriInput>/', views.detail_kategori, name='kategoriArtikel'),
    path('detail/<slug:slugInput>/', views.detail_artikel, name='detailArtikel'),
]