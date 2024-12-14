from django.db import models

# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    sport_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class FieldDetail(models.Model):
    field = models.OneToOneField(Field, on_delete=models.CASCADE, related_name="fielddetail")
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    facilities = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.field.name} Details"
