#importando a função path
from django.urls import path
#enxergando o arquivo de views
from . import views
#ele é o controller que pega um padrão de url 
#e envia para o usuario a view especifica
urlpatterns = [
    path('', views.index, name="index"),
    path('tik', views.tik, name="tik"),
    path("<int:questao_id>/", views.detalhe, name="detalhe"),
     #ex: /enquete/5/
    path("<int:questao_id>/resultados/", views.resultados, name="resultados"),
    #ex: /enquete/5/resultados/     
    path("<int:questao_id>/voto/", views.voto, name="voto"),
    #ex: /enquete/5/voto/
]

