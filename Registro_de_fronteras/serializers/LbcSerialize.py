from rest_framework import serializers
from Registro_de_fronteras.models.Lbc import Lbc

class LbcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lbc
        fields = '__all__' 
        