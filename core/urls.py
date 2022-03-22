from django.urls import path

from core.views import *

# app_name = 'core'

urlpatterns = [
    path('categorias/list/', CategoriasListAPIView.as_view(), name='categorias_list'),
    path('categorias/create/', CategoriasCreateAPIView.as_view(), name='categorias_create'),
]
