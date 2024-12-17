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


# Detail lapangan dengan daftar fasilitas terkait
def field_detail(request, field_id):
    field = get_object_or_404(Field, id=field_id)
    facilities = field.facilities.all()
    return render(request, 'sportfield/field_detail.html', {
        'field': field,            # Mengirim objek field
        'facilities': facilities   # Mengirim daftar fasilitas terkait field
    })

