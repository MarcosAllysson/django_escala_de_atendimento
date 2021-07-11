from django.contrib import admin
from posto.models import Posto


# Register your models here.
@admin.register(Posto)
class PostoAdmin(admin.ModelAdmin):
    list_display = ('nome_do_posto', 'endereco', 'ativo')
