from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from .models import Folga
from .forms import FolgaModelForm

from django.shortcuts import render
from django.contrib import messages


# Create your views here.
def home_page(request):
    print(f'REQUEST: \033[36m {request} \033[m')

    if request.method == 'POST':
        formulario = FolgaModelForm(request.POST)

        if formulario.is_valid():
            prod = formulario.save(commit=False)

            print(prod)
            messages.add_message(request, 'Sucesso')


    context = {
        'form': formulario
    }
    return render(request, 'folga/home_page.html', context)


class IndexView(ListView):
    model = Folga
    template_name = 'folga/index.html'


class CreateFolgaView(CreateView):
    model = Folga
    template_name = 'folga/folga_form.html'
    fields = '__all__'
    success_url = reverse_lazy('folga:index')


def folga_form(request):
    if request.method == 'POST':
        formulario = FolgaModelForm(request.POST)
        if formulario.is_valid():
            prod = formulario.save(commit=False)

            # dados
            dado = formulario.cleaned_data['']

            print(prod)

            # messages.success(request, 'Sucesso')
            # prod.save()

            # formulario = FolgaModelForm()

        else:
            messages.error(request, 'Erro ao salvar produto.')

    else:
        formulario = FolgaModelForm()

    context = {
        'formulario': formulario,
    }
    return render(request, 'folga/folga_form', context)

        # success_url = reverse_lazy('folga:index')


class UpdateFolgaView(UpdateView):
    model = Folga
    template_name = 'folga/folga_form.html'
    fields = '__all__'
    success_url = reverse_lazy('folga:index')


class DeleteFolgaView(DeleteView):
    model = Folga
    template_name = 'folga/folga_delete.html'
    success_url = reverse_lazy('folga:index')
