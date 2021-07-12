from django import forms
from .models import Folga


class FolgaModelForm(forms.ModelForm):
    class Meta:
        model = Folga
        fields = '__all__'
