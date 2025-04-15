from django.db import models
from .Agente import Agente
from .Usuario import Usuario
from .Frontera import Frontera


class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    numero_contrato = models.CharField(max_length=100)
    fecha_firma = models.DateField()
    fecha_inicio = models.DateField()
    cantidad_diaria_ddv = models.DecimalField(max_digits=65535, decimal_places=65535)
    estado = models.CharField(max_length=50)
    id_agente_generador = models.ForeignKey(Agente, models.DO_NOTHING, db_column='id_agente_generador')
    id_agente_comercializador = models.ForeignKey(Agente, models.DO_NOTHING, db_column='id_agente_comercializador', related_name='contrato_id_agente_comercializador_set')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_frontera = models.ForeignKey('Frontera', models.DO_NOTHING, db_column='id_frontera', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'contrato'