from rest_framework import serializers
from Registro_de_fronteras.models.Documento import Documento

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        exclude = ('id',)