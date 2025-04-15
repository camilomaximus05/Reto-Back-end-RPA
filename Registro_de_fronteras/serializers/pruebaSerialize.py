from rest_framework import serializers
from Registro_de_fronteras.models.Prueba import Prueba

class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        exclude = ('id',)