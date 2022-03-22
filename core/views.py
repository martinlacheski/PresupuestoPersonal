from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from core.models import Categorias
from core.serializers import CategoriasSerializers

class CategoriasListAPIView(ListAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializers
    
    # def to_representation(self, instance):
    #     return instance.toJSON()


class CategoriasCreateAPIView(CreateAPIView):
     serializer_class = CategoriasSerializers

