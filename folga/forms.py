from django import forms


class FolgaModelForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=10)
