from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from posto.models import Posto


# Create your views here.
class IndexView(ListView):
    model = Posto
    template_name = 'posto/index.html'


class CreatePostoView(CreateView):
    model = Posto
    fields = ['nome_do_posto', 'endereco', 'ativo']
    template_name = 'posto/posto_form.html'
    success_url = reverse_lazy('posto:index')


class UpdatePostoView(UpdateView):
    model = Posto
    fields = ['nome_do_posto', 'endereco', 'ativo']
    template_name = 'posto/posto_form.html'
    success_url = reverse_lazy('posto:index')


class DeletePostoView(DeleteView):
    model = Posto
    template_name = 'posto/posto_delete.html'
    success_url = reverse_lazy('posto:index')
