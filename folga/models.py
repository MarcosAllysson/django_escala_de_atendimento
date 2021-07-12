from django.db import models
from medico.models import Medico


# Create your models here.
class Folga(models.Model):
    medico = models.OneToOneField(Medico, on_delete=models.CASCADE)
    dia_de_folga = models.DateField(help_text='Ex: 01/01/2021', unique=True)

    def __str__(self):
        return f'{self.medico.nome} - {self.dia_de_folga.strftime("%d/%m/%Y")}'

    class Meta:
        verbose_name = 'Folga'
        verbose_name_plural = 'Folga'
