from Registro_de_fronteras.models.Lbc import Lbc
from rest_framework import viewsets, permissions
from Registro_de_fronteras.serializers.LbcSerialize import LbcSerializer

class LbcViewSet(viewsets.ModelViewSet):
    queryset = Lbc.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LbcSerializer