from django.shortcuts import render


def index(request):
    context = {
        'title':'Home',
        'heading':'Selamat Datang Di Halaman Home',
    }
    return render(request, 'index.html', context)