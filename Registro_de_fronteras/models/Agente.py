from django.db import models


class Agente(models.Model):
    nombre = models.CharField(max_length=255)
    tipo_agente = models.CharField(max_length=100)
    nit = models.CharField(max_length=50)
    correo_contacto = models.CharField(max_length=255)
    telefono_contacto = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'agente'