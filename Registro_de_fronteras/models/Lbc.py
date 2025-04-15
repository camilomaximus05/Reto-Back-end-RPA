from django.db import models
from .Frontera import Frontera

class Lbc(models.Model):
    id_lbc = models.AutoField(primary_key=True)
    fecha_calculo = models.DateField()
    metodologia = models.CharField(max_length=100)
    valor_lbc = models.FloatField()
    id_frontera = models.ForeignKey(Frontera, models.DO_NOTHING, db_column='id_frontera')

    class Meta:
        managed = False
        db_table = 'lbc'