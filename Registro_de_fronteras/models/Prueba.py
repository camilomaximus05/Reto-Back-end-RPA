from django.db import models
from .Frontera import Frontera


class Prueba(models.Model):
    id_prueba = models.AutoField(primary_key=True)
    fecha_prueba = models.DateField()
    resultado = models.CharField(max_length=100)
    tipo_prueba = models.CharField(max_length=100)
    observacion = models.TextField()
    id_frontera = models.ForeignKey(Frontera, models.DO_NOTHING, db_column='id_frontera')

    class Meta:
        # managed = False
        db_table = 'prueba'