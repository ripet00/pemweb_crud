from django.urls import path
from . import views

urlpatterns = [
     # Halaman utama
    path('', views.render_field_list, name='index'),
   
    # Halaman render daftar lapangan
    path('list/', views.render_field_list, name='render_list'),

    path('fields/', views.list_fields, name='list_fields'),                          # List Lapangan (JSON)
    path('fields/<int:field_id>/', views.field_detail, name='field_detail'),        # Detail Lapangan
    path('fields/add/', views.add_field, name='add_field'),                          # Tambah Lapangan
]
