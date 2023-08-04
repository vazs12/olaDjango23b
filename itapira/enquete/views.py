from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from.models import Questao, Resposta
from django.views import generic



# Create your views here.
class IndexView(generic.ListView):
    model = Questao
    template_name = 'enquete/index.html'


class DetalheView(generic.DetailView):
    model = Questao
    template_name = 'enquete/questao.html'

class ResultadoView(generic.DetailView):
    model = Questao
    template_name = 'enquete/resultado.html'


def voto (request,questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        resposta = questao.resposta_set.get(pk=request.POST["resposta"])
    except (KeyError, Resposta.DoesNotExist):
        return render(
            request,
            "enquete/questao.html",
            {
                "questao": questao,
                "error_message": "Está resposta não existe",
            },
        )
    else:
        resposta.votos += 1
        resposta.save()
        return HttpResponseRedirect(reverse("resultados",  args=(questao_id,)))