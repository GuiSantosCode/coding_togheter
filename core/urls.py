# urls == onde ficam as rotas do projeto


from django.urls import path
    # django.urls == modulo de urls do django
    # path == função para criar um caminho/rotas
from .views import ola_mundo
    # esta linha importa minha funcão ola_mundo do arquivo views.py


urlpatterns = [
    # urlpatterns == lista de urls do meu projeto
    
    path('', ola_mundo),
    #path == cria um caminho
    #''   == pagina principal
    #ola_mundo == função que será executada
]

