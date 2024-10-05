from django.contrib import admin

from .models import *

# Register your models here.
class artikelAdmin(admin.ModelAdmin):
    readonly_fields = ['slugArtikel']

admin.site.register(Artikel, artikelAdmin)


class kategoriAdmin(admin.ModelAdmin):
    readonly_fields = ['slugKategori']

admin.site.register(Kategori, kategoriAdmin)