from django.shortcuts import render

# Create your views here.
from .models import Artikel, Kategori

def index(request):
    articles = Artikel.objects.all()
    allKategori = Kategori.objects.all()[:6]

    context = {
        'title':'Blog',
        'heading':'Selamat Datang Di Halaman Blog',
        'Articles': articles,
        'category': allKategori,
    }
    return render(request, 'blog.html', context)


def detail_kategori(request, kategoriInput):
    articles = Artikel.objects.filter(kategori__nama=kategoriInput)

    context = {
        'title':'Kategori Article',
        'heading':'Selamat Datang Di Halaman Kategori: ' + kategoriInput.capitalize(),
        'Articles': articles,
    }
    return render(request, 'kategori.html', context)


def detail_artikel(request, slugInput):
    detail_article = Artikel.objects.get(slugArtikel=slugInput)
    allKategori = Kategori.objects.all()[:8]

    context = {
        'title':'Detail Article',
        'heading':'Selamat Datang Di Halaman Detail',
        'DetailArticle': detail_article,
        'category': allKategori,
    }
    return render(request, 'detail.html', context)