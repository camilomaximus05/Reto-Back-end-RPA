from rest_framework import serializers
from Registro_de_fronteras.models.Programacion import Programacion

class ProgramacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programacion
        exclude = ('id',)