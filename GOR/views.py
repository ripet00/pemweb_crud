from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Field, Facility

def index(request):
    return render(request, "index.html")


# Halaman utama dengan daftar nama lapangan
def render_field_list(request):
    fields = Field.objects.all()  # Ambil semua field
    return render(request, 'sportfield/list.html', {
        'fields': fields  # Kirim data field ke list.html
    })

