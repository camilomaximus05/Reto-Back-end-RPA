from rest_framework import serializers
from Registro_de_fronteras.models.Contrato import Contrato

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        exclude = ('id',)