from django.db import models
from django.utils.text import slugify

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    slugKategori =models.SlugField(editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.slugKategori = slugify(self.nama)
        return super(Kategori, self).save(*args, **kwargs)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)


class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    isi = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    slugArtikel = models.SlugField(editable=False, blank=True)
    publicDate = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slugArtikel = slugify(self.judul)
        return super(Artikel, self).save(*args, **kwargs)

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)