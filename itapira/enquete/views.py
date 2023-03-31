from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return HttpResponse("I WAS ENCHANTED TO MEET YOU")

def tik (request):
    return HttpResponse("É REAL O QUE TU SENTE?")