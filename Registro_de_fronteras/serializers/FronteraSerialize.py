from rest_framework import serializers
from Registro_de_fronteras.models.Frontera import Frontera

class FronteraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frontera
        exclude = ('id',)
        read_only_fields = ('codigo','ubicacion','tipo_frontera','estado','tipo_conexion')