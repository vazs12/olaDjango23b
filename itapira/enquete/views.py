from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from.models import Questao, Resposta



# Create your views here.
def index (request):
    ultimas_questoes = Questao.objects.order_by("-data")#[:5]
    context = {'ultimas_questoes': ultimas_questoes}
    return render(request, 'enquete/index.html', context)

def tik (request):
    return HttpResponse("É REAL O QUE TU SENTE?")

def detalhe (request,questao_id):
    # try: 
    #     questao = Questao.objects.get(pk=questao_id) # seleciona o objeto que a chave
    #                                                  #primaria tenha o valor que colocamos na url
    # except Questao.DoesNotExist:
    #   raise Http404("Questao não existe")
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'enquete/questao.html', {'questao': questao})

def resultados (request,questao_id):
    response = "Você está olhando o resultado da questão %s"
    return HttpResponse(response % questao_id)

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
        resposta.votos == 2
        resposta.save()
        return HttpResponseRedirect(reverse("enquete:resultados"),  args=(questao_id))