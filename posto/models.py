from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Posto(models.Model):
    nome_do_posto = models.CharField('Posto', max_length=120)
    endereco = models.CharField('Endereço', max_length=120)
    ativo = models.BooleanField('Ativo?', default=True)

    def __str__(self):
        return self.nome_do_posto

    def get_absolute_url(self):
        return reverse('posto:index', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['nome_do_posto']
        verbose_name = 'Posto'
        verbose_name_plural = 'Postos'
