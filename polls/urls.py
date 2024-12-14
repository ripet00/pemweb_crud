from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fields/', views.list_fields, name='list_fields'),
    path('fields/add/', views.add_field, name='add_field'),
    path('list/', views.render_list, name='render_list'),
    path('fields/<int:id>/', views.field_detail, name='field_detail'),
    path('fields/update/<int:field_id>/', views.update_field, name='update_field'), 
]