from django.forms import ModelForm
from .models import Escala


class EscalaModelForm(ModelForm):
    class Meta:
        model = Escala
        fields = '__all__'
