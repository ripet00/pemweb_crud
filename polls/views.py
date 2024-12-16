from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Field, Facility

def index(request):
    return render(request, "index.html")


# Halaman utama dengan daftar nama lapangan
def render_field_list(request):
    return render(request, 'sportfield/list.html')


# Daftar lapangan
def list_fields(request):
    fields = Field.objects.all()
    data = [
        {
            'id': field.id,
            'name': field.name,
            'sport_type': field.sport_type,
            # 'location': field.location,
            # 'operating_hours': field.operating_hours,
            # 'price_per_hour': float(field.price_per_hour),
            # 'is_available': field.is_available,
        }
        for field in fields
    ]
    return JsonResponse(data, safe=False)


# Detail lapangan dengan daftar fasilitas terkait
def field_detail(request, field_id):
    field = get_object_or_404(Field, id=field_id)
    facilities = field.facilities.all()
    # data = {
    #     'field': {
    #         'id': field.id,
    #         'name': field.name,
    #         'location': field.location,
    #         'sport_type' : field.sport_type,
    #         'operating_hours': field.operating_hours,
    #         'price_per_hour': float(field.price_per_hour),
    #         'is_available': field.is_available,
    #     },
    #     'facilities': [
    #         {
    #             'id': facility.id,
    #             'name': facility.name,
    #             'description': facility.description,
    #             'is_available': facility.is_available,
    #         }
    #         for facility in facilities
    #     ]
    # }
    # return JsonResponse(data)
    # Kirim data ke template
    return render(request, 'sportfield/field_detail.html', {
        'field': field,            # Mengirim objek field
        'facilities': facilities   # Mengirim daftar fasilitas terkait field
    })


# Tambah lapangan
def add_field(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        sport_type = request.POST['sport_type']
        operating_hours = request.POST['operating_hours']
        price_per_hour = request.POST['price_per_hour']
        is_available = request.POST['is_available'] == 'true'

        field = Field.objects.create(
            name=name,
            location=location,
            sport_type=sport_type,
            operating_hours=operating_hours,
            price_per_hour=price_per_hour,
            is_available=is_available,
        )
        return JsonResponse({'message': 'Lapangan berhasil ditambahkan!'})


# # Edit Lapangan
# def edit_field(request, field_id):
#     if request.method == 'POST':
#         try:
#             field = Field.objects.get(id=field_id)
#             field.name = request.POST.get('name', field.name)
#             field.location = request.POST.get('location', field.location)
#             field.operating_hours = request.POST.get('operating_hours', field.operating_hours)
#             field.price_per_hour = request.POST.get('price_per_hour', field.price_per_hour)
#             field.is_available = request.POST.get('is_available', 'false') == 'true'
#             field.save()

#             return JsonResponse({'message': 'Lapangan berhasil diperbarui!'}, status=200)
#         except Field.DoesNotExist:
#             return JsonResponse({'message': 'Lapangan tidak ditemukan!'}, status=404)
#         except Exception as e:
#             return JsonResponse({'message': 'Terjadi kesalahan: ' + str(e)}, status=400)
#     return JsonResponse({'message': 'Metode tidak diizinkan!'}, status=405)



# # Hapus lapangan
# def delete_field(request, field_id):
#     if request.method == 'POST':
#         try:
#             field = Field.objects.get(id=field_id)
#             field.delete()
#             return JsonResponse({'message': 'Lapangan berhasil dihapus!'})
#         except Field.DoesNotExist:
#             return JsonResponse({'message': 'Lapangan tidak ditemukan!'}, status=404)
#         except Exception as e:
#             return JsonResponse({'message': 'Terjadi kesalahan: ' + str(e)}, status=400)
#     return JsonResponse({'message': 'Metode tidak diizinkan!'}, status=405)

# Tambah fasilitas
def add_facility(request, field_id):
    if request.method == 'POST':
        field = get_object_or_404(Field, id=field_id)
        name = request.POST['name']
        description = request.POST['description']
        is_available = request.POST['is_available'] == 'true'

        Facility.objects.create(
            field=field,
            name=name,
            description=description,
            is_available=is_available,
        )
        return JsonResponse({'message': 'Fasilitas berhasil ditambahkan!'})


# # Edit Fasilitas
# def edit_facility(request, facility_id):
#     if request.method == 'POST':
#         try:
#             facility = Facility.objects.get(id=facility_id)
#             facility.name = request.POST.get('name', facility.name)
#             facility.description = request.POST.get('description', facility.description)
#             facility.is_available = request.POST.get('is_available', 'false') == 'true'
#             facility.save()

#             return JsonResponse({'message': 'Fasilitas berhasil diperbarui!'}, status=200)
#         except Facility.DoesNotExist:
#             return JsonResponse({'message': 'Fasilitas tidak ditemukan!'}, status=404)
#         except Exception as e:
#             return JsonResponse({'message': 'Terjadi kesalahan: ' + str(e)}, status=400)
#     return JsonResponse({'message': 'Metode tidak diizinkan!'}, status=405)


# # Hapus fasilitas
# def delete_facility(request, facility_id):
#     if request.method == 'POST':
#         try:
#             facility = Facility.objects.get(id=facility_id)
#             facility.delete()
#             return JsonResponse({'message': 'Fasilitas berhasil dihapus!'})
#         except Facility.DoesNotExist:
#             return JsonResponse({'message': 'Fasilitas tidak ditemukan!'}, status=404)
#         except Exception as e:
#             return JsonResponse({'message': 'Terjadi kesalahan: ' + str(e)}, status=400)
#     return JsonResponse({'message': 'Metode tidak diizinkan!'}, status=405)


