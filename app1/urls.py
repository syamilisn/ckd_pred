"""CUSTOM"""
from django.urls import path
from .views import index, input, export, dataset, predict, importcsv
app_name = 'app1'

urlpatterns = [
    path('', index, name = 'index'),
    path('input/', input, name = 'input'),
    path('export/', export, name = 'export'),
    path('dataset/', dataset, name = 'dataset'),
    path('predict/', predict, name = 'predict'),
    path('importcsv/', importcsv, name = 'importcsv'),
]