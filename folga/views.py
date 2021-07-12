from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from .models import Folga
from medico.models import Medico
from escala.models import Escala
from .forms import FolgaModelForm

from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime, date


# Create your views here.
class IndexView(ListView):
    model = Folga
    template_name = 'folga/index.html'


def create_folga(request):
    formulario = FolgaModelForm(request.POST)

    if request.method == 'POST':

        if formulario.is_valid():
            medico = request.POST.get('medico')
            folga = request.POST.get('dia_de_folga')

            # de string pra date
            fdt = datetime.strptime(folga, '%d/%m/%Y').date()
            # data de hoje
            hoje = date.today()

            # Verificando dia da folga.
            if fdt >= hoje:
                try:
                    # analisando se o médico está ativo
                    medico_qs = Medico.objects.get(id=medico)
                    medico_status = medico_qs.ativo

                    # analisando se não está em escala
                    medico_escala_qs = Escala.objects.filter(medico_id=medico)

                    if medico_status and len(medico_escala_qs) == 0:
                        # salvando dados
                        formulario.save()

                        # redirecionando
                        return redirect('folga:index')

                    else:
                        messages.error(request, 'Médico não pode folgar. Está inativo, em escala ou não foi encontrado.')

                except Exception:
                    messages.error(request, 'Opa, houve um erro...')

            else:
                messages.error(request, 'Esta data já passou.')

        else:
            messages.error(request, 'Houve algum erro, tente novamente.')

    else:
        formulario = FolgaModelForm()

    context = {
        'form': formulario
    }

    return render(request, 'folga/folga_form.html', context)


def update_folga(request, pk):
    folga = Folga.objects.get(id=pk)
    form = FolgaModelForm(instance=folga)

    if request.method == 'POST':
        form = FolgaModelForm(request.POST, instance=folga)

        if form.is_valid():
            medico = request.POST.get('medico')
            folga = request.POST.get('dia_de_folga')

            # de string pra date
            fdt = datetime.strptime(folga, '%d/%m/%Y').date()
            # data de hoje
            hoje = date.today()

            # Verificando dia da folga.
            if fdt >= hoje:
                try:
                    # analisando se o médico está ativo
                    medico_qs = Medico.objects.get(id=medico)
                    medico_status = medico_qs.ativo

                    # analisando se não está em escala
                    medico_escala_qs = Escala.objects.filter(medico_id=medico)

                    if medico_status and len(medico_escala_qs) == 0:
                        # salvando dados
                        form.save()

                        # redirecionando
                        return redirect('folga:index')

                    else:
                        messages.error(request,
                                       'Médico não pode folgar. Está inativo, em escala ou não foi encontrado.')

                except Exception as e:
                    messages.error(request, 'Opa, houve um erro...')

            else:
                messages.error(request, 'Esta data já passou.')

        else:
            messages.error(request, 'Houve algum erro, tente novamente.')

    context = {
        'form': form
    }

    return render(request, 'folga/folga_form.html', context)


class DeleteFolgaView(DeleteView):
    model = Folga
    template_name = 'folga/folga_delete.html'
    success_url = reverse_lazy('folga:index')
