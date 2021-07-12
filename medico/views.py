from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Medico

from .forms import MedicoModelForm
from posto.models import Posto
from django.contrib import messages


# Create your views here.
class IndexView(ListView):
    model = Medico
    template_name = 'medico/index.html'


def create_medico(request):
    formulario = MedicoModelForm(request.POST)

    if request.method == 'POST':

        if formulario.is_valid():
            posto = request.POST.get('posto_de_trabalho')

            # analisando se o posto está ativo
            try:
                posto_qs = Posto.objects.get(id=posto)
                posto_status = posto_qs.ativo

                if posto_status:
                    # salvando dados
                    formulario.save()

                    # redirecionando usuário
                    return redirect('medicos:index')

                else:
                    messages.error(request, 'Posto de trabalho inativo.')

            except Exception as e:
                messages.error(request, 'Houve algum erro, tente novamente.')

        else:
            messages.error(request, 'Houve algum erro, tente novamente.')

    else:
        formulario = MedicoModelForm()

    context = {
        'form': formulario
    }

    return render(request, 'medico/medico_form.html', context)


def update_medico(request, pk):
    medico = Medico.objects.get(pk=pk)
    formulario = MedicoModelForm(instance=medico)

    if request.method == 'POST':
        formulario = MedicoModelForm(request.POST, instance=medico)

        if formulario.is_valid():
            posto = request.POST.get('posto_de_trabalho')

            # analisando se o posto está ativo
            try:
                posto_qs = Posto.objects.get(id=posto)
                posto_status = posto_qs.ativo

                if posto_status:
                    # salvando dados
                    formulario.save()

                    # redirecionando usuário
                    return redirect('medicos:index')

                else:
                    messages.error(request, 'Posto de trabalho inativo.')

            except Exception as e:
                messages.error(request, 'Houve algum erro, tente novamente.')

        else:
            messages.error(request, 'Houve algum erro, tente novamente.')

    context = {
        'form': formulario
    }

    return render(request, 'medico/medico_form.html', context)
