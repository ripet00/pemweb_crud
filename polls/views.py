from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Field, FieldDetail


def index(request):
    return render(request, "index.html")


def render_list(request):
    return render(request, "sportfield/list.html")


def list_fields(request):
    fields = Field.objects.all()
    data = [
        {
            "id": field.id,
            "name": field.name,
            "location": field.location,
            "sport_type": field.sport_type,
            "price_per_hour": field.fielddetail.price_per_hour,
            "facilities": field.fielddetail.facilities,
            "is_available": field.fielddetail.is_available,
        }
        for field in fields
    ]
    return JsonResponse(data, safe=False)


def add_field(request):
    if request.method == "POST":
        # Data dari AJAX
        name = request.POST["name"]
        location = request.POST["location"]
        sport_type = request.POST["sport_type"]
        price_per_hour = request.POST["price_per_hour"]
        facilities = request.POST["facilities"]
        is_available = request.POST["is_available"] == "true"

        # Simpan Field dan FieldDetail
        field = Field.objects.create(
            name=name, location=location, sport_type=sport_type
        )
        FieldDetail.objects.create(
            field=field,
            price_per_hour=price_per_hour,
            facilities=facilities,
            is_available=is_available,
        )
        return JsonResponse({"message": "Field berhasil ditambahkan!"})


def field_detail(request, id):
    field = get_object_or_404(Field, id=id)  # Mencari lapangan berdasarkan ID
    field_detail = field.fielddetail  # Mengakses FieldDetail terkait

    return render(
        request,
        "sportfield/field_detail.html",
        {
            "field": field,
            "field_detail": field_detail,
        },
    )


def update_field(request, field_id):
    if request.method == "POST":
        try:
            field = Field.objects.get(id=field_id)
            field.name = request.POST.get("name")
            field.location = request.POST.get("location")
            field.sport_type = request.POST.get("sport_type")
            field.fielddetail.price_per_hour = request.POST.get("price_per_hour")
            field.fielddetail.facilities = request.POST.get("facilities")
            field.fielddetail.is_available = request.POST.get("is_available") == "on"
            field.save()
            field.fielddetail.save()
            return JsonResponse(
                {"message": "Lapangan berhasil diperbarui!"}, status=200
            )
        except Field.DoesNotExist:
            return JsonResponse({"message": "Lapangan tidak ditemukan!"}, status=404)
        except Exception as e:
            return JsonResponse({"message": "Terjadi kesalahan: " + str(e)}, status=400)
    return JsonResponse({"message": "Metode tidak diizinkan!"}, status=405)


def delete_field(request, field_id):
    if request.method == "POST":
        try:
            field = Field.objects.get(id=field_id)
            field.delete()
            return JsonResponse({"message": "Lapangan berhasil dihapus!"}, status=200)
        except Field.DoesNotExist:
            return JsonResponse({"message": "Lapangan tidak ditemukan!"}, status=404)
        except Exception as e:
            return JsonResponse({"message": "Terjadi kesalahan: " + str(e)}, status=400)
    return JsonResponse({"message": "Metode tidak diizinkan!"}, status=405)
