from django.contrib import admin
from .models import Escala


# Register your models here.
@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ('medico', 'posto_de_trabalho', 'data')
