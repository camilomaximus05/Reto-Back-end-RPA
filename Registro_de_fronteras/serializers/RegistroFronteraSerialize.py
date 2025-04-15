from rest_framework import serializers
from Registro_de_fronteras.models.RegistroFrontera import RegistroFrontera

class RegistroFronteraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroFrontera
        exclude = ('id',)