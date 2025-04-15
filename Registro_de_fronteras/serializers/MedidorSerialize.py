from rest_framework import serializers
from Registro_de_fronteras.models.Medidor import Medidor

class MedidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        exclude = ('id',)