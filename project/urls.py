"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import index, home, create, store, painel, dologin, logouts, changePassword, inicial, material, rendimento, aulas, hardware, aposthdw, eletrica, apostele, automacao, apostauto, mecanica, apostmec, config

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', home, name="home"),
    path('create/', create),
    path('store/', store),
    path('painel/', painel),
    path('dologin/', dologin),
    path('logouts/', logouts),
    path('password/', changePassword),
    path('inicial/', inicial, name="inicial"),
    path('material/', material, name="material"),
    path('rendimento/', rendimento, name="rendimento"),
    path('aulas/', aulas, name="aulas"),
    path('hardware/', hardware, name="hardware"),
    path('apostilahardware/', aposthdw, name="aposthdw"),
    path('eletrica/', eletrica, name="eletrica"),
    path('apostilaeletrica/', apostele, name="apostele"),
    path('automacao/', automacao, name="automacao"),
    path('apostilaauto/', apostauto, name="apostauto"),
    path('mecanica/', mecanica, name="mecanica"),
    path('apostilamec/', apostmec, name="apostmec"),
    path('config/', config, name="config"),
]
