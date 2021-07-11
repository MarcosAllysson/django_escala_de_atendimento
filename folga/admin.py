from django.contrib import admin
from .models import Folga


# Register your models here.
@admin.register(Folga)
class FolgaAdmin(admin.ModelAdmin):
    list_display = ('medico', 'dia_de_folga')
