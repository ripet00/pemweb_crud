from django.db import models

# Model untuk Lapangan
class Field(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    sport_type = models.CharField(max_length=50)
    operating_hours = models.CharField(max_length=50)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Model untuk Fasilitas
class Facility(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="facilities")
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({'Tersedia' if self.is_available else 'Tidak Tersedia'})"

