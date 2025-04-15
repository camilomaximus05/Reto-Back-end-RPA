from django.db import models
from .Frontera import Frontera

class RegistroFrontera(models.Model):
    id_registro = models.AutoField(primary_key=True)
    fecha_registro = models.DateField()
    estado = models.CharField(max_length=50)
    observacion = models.TextField()
    id_frontera = models.ForeignKey(Frontera, models.DO_NOTHING, db_column='id_frontera')

    class Meta:
        # managed = False
        db_table = 'registro_frontera'
