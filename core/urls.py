# urls == onde ficam as rotas do projeto


from django.urls import path
    # django.urls == modulo de urls do django
    # path == função para criar um caminho/rotas
from .views import pagina_um, pagina_dois
    # esta linha importa minha funcão ola_mundo do arquivo views.py


urlpatterns = [
    # urlpatterns == lista de urls do meu projeto
    
    path('', pagina_um, name='url_pagina_um'),
    
    
    path('assuidade/', pagina_dois, name='url_pagina_dois')
]

