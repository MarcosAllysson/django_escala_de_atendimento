from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import Escala

from django.contrib import messages
from .forms import EscalaModelForm
from medico.models import Medico
from posto.models import Posto
from folga.models import Folga
from datetime import datetime, date


# Create your views here.
class HomeView(TemplateView):
    template_name = 'escala/home_page.html'


class ListEscalaView(ListView):
    model = Escala
    template_name = 'escala/index.html'


def create_escala(request):
    formulario = EscalaModelForm(request.POST)

    if request.method == 'POST':

        if formulario.is_valid():
            medico = request.POST.get('medico')
            posto = request.POST.get('posto_de_trabalho')
            data = request.POST.get('data')

            # de string pra date
            data_escala = datetime.strptime(data, '%d/%m/%Y').date()
            # data de hoje
            hoje = date.today()

            # Verificando dia da escala.
            if data_escala >= hoje:
                try:
                    # analisando se o médico está ativo
                    medico_qs = Medico.objects.get(id=medico)
                    medico_status = medico_qs.ativo

                    # analisando se não está em escala
                    medico_escala_qs = Escala.objects.filter(medico_id=medico)

                    # analisando se não está de folga
                    folga_qs = Folga.objects.filter(medico_id=medico, dia_de_folga=data_escala)
                    medico_disponivel = False

                    if len(folga_qs) > 0:
                        if folga_qs[0].dia_de_folga != data_escala:
                            medico_disponivel = True
                        else:
                            messages.error(request, 'Não é possível, pois a data da escala do médico é igual da folga.')
                    else:
                        medico_disponivel = True

                    # analisando se o posto está ativo
                    posto_qs = Posto.objects.get(id=posto)
                    posto_status = posto_qs.ativo

                    if medico_status and len(medico_escala_qs) == 0 and medico_disponivel and posto_status:
                        # salvando dados
                        formulario.save()

                        # redirecionando
                        return redirect('escala:escala')

                    else:
                        messages.error(request, 'Verifique se posto de trabalho e médico estão ativos / aptos.')

                except Exception as e:
                    messages.error(request, f'Opa, houve um erro: {e}...')

            else:
                messages.error(request, 'Esta data já passou.')

        else:
            messages.error(request, 'Houve algum erro, tente novamente.')

    else:
        formulario = EscalaModelForm()

    context = {
        'form': formulario
    }

    return render(request, 'escala/escala_form.html', context)


def update_escala(request, pk):
    escala = Escala.objects.get(pk=pk)
    formulario = EscalaModelForm(instance=escala)

    if request.method == 'POST':
        formulario = EscalaModelForm(request.POST, instance=escala)

        if formulario.is_valid():
            medico = request.POST.get('medico')
            posto = request.POST.get('posto_de_trabalho')
            data = request.POST.get('data')

            # de string pra date
            data_escala = datetime.strptime(data, '%d/%m/%Y').date()
            # data de hoje
            hoje = date.today()

            # Verificando dia da escala.
            if data_escala >= hoje:
                try:
                    # analisando se o médico está ativo
                    medico_qs = Medico.objects.get(id=medico)
                    medico_status = medico_qs.ativo
                    medico_disponivel = False

                    # analisando escala do médico
                    medico_escala_qs = Escala.objects.filter(medico_id=medico)

                    if len(medico_escala_qs) > 0:
                        if medico_escala_qs[0].data != data_escala:
                            medico_disponivel = True
                        else:
                            messages.error(request, 'Coloque uma data diferente da atual.')
                    else:
                        medico_disponivel = True

                    # analisando se não está de folga
                    folga_qs = Folga.objects.filter(medico_id=medico, dia_de_folga=data_escala)

                    if len(folga_qs) > 0:
                        if folga_qs[0].dia_de_folga != data_escala:
                            medico_disponivel = True
                        else:
                            messages.error(request, 'Não é possível, pois a data da escala do médico é igual da folga.')
                    else:
                        medico_disponivel = True

                    # analisando se o posto está ativo
                    posto_qs = Posto.objects.get(id=posto)
                    posto_status = posto_qs.ativo

                    if medico_status and medico_disponivel and posto_status:
                        # salvando dados
                        formulario.save()

                        # redirecionando
                        return redirect('escala:escala')

                    else:
                        messages.error(request, 'Verifique se posto de trabalho e médico estão ativos / aptos.')

                except Exception:
                    messages.error(request, 'Opa, houve um erro...')

            else:
                messages.error(request, 'Esta data já passou.')

        else:
            messages.error(request, 'Houve algum erro, tente novamente.')

    context = {
        'form': formulario
    }

    return render(request, 'escala/escala_form.html', context)


class DeleteEscalaView(DeleteView):
    model = Escala
    template_name = 'escala/escala_delete.html'
    success_url = reverse_lazy('escala:escala')
