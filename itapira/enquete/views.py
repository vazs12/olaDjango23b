from django.shortcuts import render
from django.http import HttpResponse
from.models import Questao

# Create your views here.
def index (request):
    ultimas_questoes = Questao.objects.order_by("-data")[:5]
    saida =", ".join([q.pergunta for q in ultimas_questoes])
    return HttpResponse(saida)

def tik (request):
    return HttpResponse("É REAL O QUE TU SENTE?")

def detalhe (request,questao_id):
    return HttpResponse("Você está olhando a questão %s" % questao_id)

def resultados (request,questao_id):
    response = "Você está olhando o resultado da questão %s"
    return HttpResponse(response % questao_id)

def voto (request,questao_id):
    return HttpResponse("Você está votando na questão %s" % questao_id)