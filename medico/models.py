from django.db import models
from django.shortcuts import reverse
from posto.models import Posto


# Create your models here.
class Medico(models.Model):
    nome = models.CharField('Médico', max_length=20)
    sobrenome = models.CharField('Sobrenome', max_length=20)
    data_de_admissao = models.DateField(auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    posto_de_trabalho = models.ForeignKey(Posto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

    def get_absolute_url(self):
        return reverse('medicos:index', kwargs={'pk': self.pk})

    class Meta:
        # Ordenando pelo nome
        ordering = ['nome']
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
