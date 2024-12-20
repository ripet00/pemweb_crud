# Generated by Django 5.1.2 on 2024-12-14 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fasilitas",
            fields=[
                ("id_fasilitas", models.AutoField(primary_key=True, serialize=False)),
                ("nama", models.CharField(max_length=100)),
                ("deskripsi", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Lapangan",
            fields=[
                ("id_lapangan", models.AutoField(primary_key=True, serialize=False)),
                ("nama", models.CharField(max_length=100)),
                ("lokasi", models.CharField(max_length=100)),
                ("harga", models.DecimalField(decimal_places=2, max_digits=10)),
                ("waktu", models.TimeField()),
                ("olahraga", models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
