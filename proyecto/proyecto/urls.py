"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from proyecto_app import views#importa la vista desde la applicacion
from modernrpc.views import RPCEntryPoint#importa un punto de entrada para los servicios

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('calculadora/',views.get_suma),
    path('rpc/',RPCEntryPoint.as_view()),
    path('calculadora/<int:a>/<int:b>',views.rpcAdd,name='rpcAdd'),
]
