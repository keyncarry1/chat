from django.db import models

# Create your models here.
class usuario(models.Model):
    usuario = models.CharField(max_length=50)
    contra = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.usuario} {self.contra}'

class cesfam(models.Model):
    rut = models.IntegerField
    cesfam = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)

    def __str__(self):
            return f'{self.rut} {self.cesfam} {self.sector}'