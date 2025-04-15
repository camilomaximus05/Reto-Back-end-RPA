from django.db import models



class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=100)
    url = models.TextField()
    fecha_emision = models.DateField()
    id_registro = models.ForeignKey('RegistroFrontera', models.DO_NOTHING, db_column='id_registro')

    class Meta:
        # managed = False
        db_table = 'documento'