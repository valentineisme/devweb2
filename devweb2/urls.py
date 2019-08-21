"""devweb2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django.conf import settings

from dev2 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),

    #usuario
    url(r'^cadastro_usuario/$', views.cadastro_usuario, name='cadastro_usuario'),
    url(r'^logar/$', views.logar, name='logar'),
    url(r'^validacao/$', views.validacao, name='validacao'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^sair/$', views.sair, name='sair'),

    url(r'^sobre/$', views.sobre, name='sobre'),
]
