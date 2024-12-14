from django.db import models


class Lapangan(models.Model):
    id_lapangan = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    waktu = models.TimeField()
    olahraga = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.id_lapangan


class Fasilitas(models.Model):
    id_fasilitas = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self):
        return self.id_fasilitas
