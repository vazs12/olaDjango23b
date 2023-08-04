#importando a função path
from django.urls import path
#enxergando o arquivo de views
from . import views
#ele é o controller que pega um padrão de url 
#e envia para o usuario a view especifica
urlpatterns = [
    path('', views.index, name="index"),
    path('tik', views.tik, name="tik"),
    path("<int:pk>/", views.DetalheView.as_view(), name="detalhe"),
     #ex: /enquete/5/
    path("<int:pk>/resultados/", views.ResultadoView.as_view(), name="resultados"),
    #ex: /enquete/5/resultados/     
    path("<int:questao_id>/voto/", views.voto, name="voto"),
    #ex: /enquete/5/voto/
]

