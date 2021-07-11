from django.db import models
from django.shortcuts import reverse
from medico.models import Medico
from posto.models import Posto


# Create your models here.
class Escala(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    posto_de_trabalho = models.ForeignKey(Posto, on_delete=models.CASCADE)
    data = models.DateField(help_text='Ex: 01/01/2021')

    def get_absolute_url(self):
        return reverse('escala:index', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.medico.nome} - {self.posto_de_trabalho.nome_do_posto} - {self.data.strftime("%d/%m/%Y")}'

    class Meta:
        verbose_name = 'Escala'
        verbose_name_plural = 'Escalas'
        ordering = ['data']
