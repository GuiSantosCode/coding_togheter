"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#include == permite usar urls de outros apps

urlpatterns = [
    path('admin/', admin.site.urls),
        # 'admin/' == endereço do painel admin
        # admin.site.urls == URLs prontas do admin do Django
    
    path('', include('core.urls')),
        # '' == página inicial do projeto
        # include() == inclui URLs de outro arquivo
        # 'core.urls' == pega as URLs do arquivo: core/urls.py
    ]
