from django.shortcuts import render

from .forms import KontakForms

# Create your views here.
def index(request):
    kontak_form = KontakForms()
    context = {
        'title':'Kontak',
        'heading':'Kontak Form',
        'f_kontak':kontak_form,
    }
    print(request.POST)
    return render(request, 'kontak.html', context)