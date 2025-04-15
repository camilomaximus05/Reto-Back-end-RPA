from django.db import models
from .Frontera import Frontera


class Medidor(models.Model):
    id_medidor = models.AutoField(primary_key=True)
    numero_serie = models.CharField(max_length=100)
    tipo_medidor = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    capacidad_interrogacion_remota = models.BooleanField()
    estado = models.CharField(max_length=50)
    id_frontera = models.ForeignKey(Frontera, models.DO_NOTHING, db_column='id_frontera')

    class Meta:
        # managed = False
        db_table = 'medidor'
