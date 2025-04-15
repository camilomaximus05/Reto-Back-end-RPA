from Registro_de_fronteras.models.Frontera import Frontera
from rest_framework import viewsets, permissions
from Registro_de_fronteras.serializers.FronteraSerialize import FronteraSerializer

class FronteraViewSet(viewsets.ModelViewSet):
    queryset = Frontera.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FronteraSerializer