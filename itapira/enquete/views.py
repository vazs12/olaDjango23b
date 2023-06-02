from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from.models import Questao

# Create your views here.
def index (request):
    ultimas_questoes = Questao.objects.order_by("-data")[:5]
    context = {'ultimas_questoes': ultimas_questoes}
    return render(request, 'enquete/index.html', context)

def tik (request):
    return HttpResponse("É REAL O QUE TU SENTE?")

def detalhe (request,questao_id):
    try: 
        questao = Questao.objects.get(pk=questao_id) # seleciona o objeto que a chave
                                                     #primaria tenha o valor que colocamos na url
    except Questao.DoesNotExist:
        raise Http404("Questao não existe")
    return render(request, 'enquete/questao.html', {'questao': questao})

def resultados (request,questao_id):
    response = "Você está olhando o resultado da questão %s"
    return HttpResponse(response % questao_id)

def voto (request,questao_id):
    return HttpResponse("Você está votando na questão %s" % questao_id)