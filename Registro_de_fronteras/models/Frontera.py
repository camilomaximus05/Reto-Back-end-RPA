from django.db import models
from .Agente import Agente
from .Usuario import Usuario

class Frontera(models.Model):
    codigo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    tipo_frontera = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True, blank=True,db_column='id_usuario')
    id_agente = models.ForeignKey('Agente', on_delete=models.CASCADE, null=True, blank=True,db_column='id_agente')
    tipo_conexion = models.CharField(max_length=100)

    class Meta:
        # managed = False
        db_table = 'frontera'