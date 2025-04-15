from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    documento_identidad = models.CharField()
    correo = models.CharField(max_length=255)
    telefono_contacto = models.CharField()

    class Meta:
        # managed = False
        db_table = 'usuario'