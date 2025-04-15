from django.db import models
from .Contrato import Contrato


class Programacion(models.Model):
    id_programa = models.AutoField(primary_key=True)
    nombre_programa = models.CharField(max_length=255)
    tipo_activacion = models.CharField(max_length=100)
    periodos_prueba = models.IntegerField()
    id_contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='id_contrato')
    hora_de_inicio = models.TimeField()
    hora_de_fin = models.TimeField(blank=True, null=True)
    horario = models.CharField(max_length=100)

    class Meta:
        # managed = False
        db_table = 'programacion'