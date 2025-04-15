from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers.FormularioSerialize import FormularioFronteraSerializer
from ..models.RegistroFrontera import RegistroFrontera

class FormularioFronteraView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        registros = RegistroFrontera.objects.all().select_related('usuario', 'frontera', 'lbc', 'documento', 'medidor')
        if registros.exists():
            serializer = FormularioFronteraSerializer(registros.first())
            return Response(serializer.data)
        return Response({"error": "No hay registros disponibles."})
