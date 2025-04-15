from rest_framework import serializers
from Registro_de_fronteras.models.Agente import Agente

class AgenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente
        exclude = ('id',)
        