from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Medico


# Create your views here.
class IndexView(ListView):
    model = Medico
    template_name = 'medico/index.html'


class CreateMedicoView(CreateView):
    model = Medico
    template_name = 'medico/medico_form.html'
    fields = '__all__'
    success_url = reverse_lazy('medicos:index')


class UpdateMedicoView(UpdateView):
    model = Medico
    template_name = 'medico/medico_form.html'
    fields = '__all__'
    success_url = reverse_lazy('medicos:index')


class DeleteMedicoView(DeleteView):
    model = Medico
    template_name = 'medico/medico_delete.html'
    success_url = reverse_lazy('medicos:index')
