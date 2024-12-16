from django.urls import path
from . import views

urlpatterns = [
    # Halaman utama
    path('', views.render_field_list, name='index'),
   
    # Halaman render daftar lapangan
    path('list/', views.render_field_list, name='render_list'),

    # CRUD Lapangan
    path('fields/', views.list_fields, name='list_fields'),               # List Lapangan (JSON)
    path('fields/add/', views.add_field, name='add_field'),               # Tambah Lapangan
    path('fields/<int:field_id>/', views.field_detail, name='field_detail'),  # Detail Lapangan
    # path('fields/update/<int:field_id>/', views.edit_field, name='edit_field'),  # Edit Lapangan
    # path('fields/delete/<int:field_id>/', views.delete_field, name='delete_field'),  # Hapus Lapangan

    # CRUD Fasilitas
    path('fields/<int:field_id>/facilities/add/', views.add_facility, name='add_facility'),  # Tambah Fasilitas
    # path('facilities/update/<int:facility_id>/', views.edit_facility, name='edit_facility'),  # Edit Fasilitas
    # path('facilities/delete/<int:facility_id>/', views.delete_facility, name='delete_facility'),  # Hapus Fasilitas

]
