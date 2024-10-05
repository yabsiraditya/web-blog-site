from django.shortcuts import render

# Create your views here.
from .models import Artikel

def index(request):
    articles = Artikel.objects.all()

    context = {
        'title':'Blog',
        'heading':'Selamat Datang Di Halaman Blog',
        'Articles': articles,
    }
    return render(request, 'blog.html', context)


def detail_artikel(request, slugInput):
    detail_article = Artikel.objects.get(slugArtikel=slugInput)

    context = {
        'title':'Detail Article',
        'heading':'Selamat Datang Di Halaman Detail',
        'DetailArticle': detail_article,
    }
    return render(request, 'detail.html', context)