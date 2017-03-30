from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cadastro_cliente/', views.cadastro, name='cadastro'),
    url(r'^lista_dos_clientes/', views.lista_cliente, name='index'),
]