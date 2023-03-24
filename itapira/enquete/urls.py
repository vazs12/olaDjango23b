#importando a função path
from django.urls import path
#enxergando o arquivo de views
from . import views
#ele é o controller que pega um padrão de url 
#e envia para o usuario a view especifica
urlpatterns = [
    path('', views.index, nome="index"),
]
