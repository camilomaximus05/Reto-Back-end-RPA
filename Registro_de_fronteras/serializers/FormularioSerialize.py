from rest_framework import serializers
from ..models import RegistroFrontera, Frontera, Usuario, Lbc, Documento
from django.utils.timezone import now

class FormularioSerializer(serializers.ModelSerializer):
    nombre_solicitante = serializers.SerializerMethodField()
    fecha_solicitud = serializers.SerializerMethodField()
    nombre_frontera = serializers.SerializerMethodField()
    ubicacion = serializers.SerializerMethodField()
    nombre_usuario = serializers.SerializerMethodField()
    email_usuario = serializers.SerializerMethodField()
    tipo_medidor = serializers.SerializerMethodField()
    serie_medidor = serializers.SerializerMethodField()
    tipo_curva = serializers.SerializerMethodField()
    parametros_curva = serializers.SerializerMethodField()
    certificacion_num = serializers.SerializerMethodField()
    entidad_certificadora = serializers.SerializerMethodField()

    class Meta:
        model = RegistroFrontera
        fields = [
            'nombre_solicitante', 'fecha_solicitud',
            'nombre_frontera', 'ubicacion',
            'nombre_usuario', 'email_usuario',
            'tipo_medidor', 'serie_medidor',
            'tipo_curva', 'parametros_curva',
            'certificacion_num', 'entidad_certificadora'
        ]

    def get_nombre_solicitante(self, obj):
        return obj.usuario.nombre

    def get_fecha_solicitud(self, obj):
        return now().date()

    def get_nombre_frontera(self, obj):
        return f"Frontera #{obj.frontera.id}"

    def get_ubicacion(self, obj):
        return obj.frontera.ubicacion if hasattr(obj.frontera, 'ubicacion') else ""

    def get_nombre_usuario(self, obj):
        return obj.usuario.nombre

    def get_email_usuario(self, obj):
        return obj.usuario.email

    def get_tipo_medidor(self, obj):
        return obj.medidor.tipo if hasattr(obj, 'medidor') else ""

    def get_serie_medidor(self, obj):
        return obj.medidor.serie if hasattr(obj, 'medidor') else ""

    def get_tipo_curva(self, obj):
        return obj.lbc.tipo_curva if hasattr(obj, 'lbc') else ""

    def get_parametros_curva(self, obj):
        return obj.lbc.parametros if hasattr(obj, 'lbc') else ""

    def get_certificacion_num(self, obj):
        return obj.documento.id if hasattr(obj, 'documento') else ""

    def get_entidad_certificadora(self, obj):
        return "CREG"