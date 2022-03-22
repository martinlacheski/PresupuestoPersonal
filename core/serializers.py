from rest_framework import serializers

from core.models import Categorias

class CategoriasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'