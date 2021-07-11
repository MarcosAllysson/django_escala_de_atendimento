from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Escala


# Create your views here.
class IndexView(ListView):
    model = Escala
    template_name = 'escala/index.html'


class CreateEscalaView(CreateView):
    model = Escala
    template_name = 'escala/escala_form.html'
    fields = '__all__'
    success_url = reverse_lazy('escala:index')


class UpdateEscalaView(UpdateView):
    model = Escala
    template_name = 'escala/escala_form.html'
    fields = '__all__'
    success_url = reverse_lazy('escala:index')


class DeleteEscalaView(DeleteView):
    model = Escala
    template_name = 'escala/escala_delete.html'
    success_url = reverse_lazy('escala:index')
