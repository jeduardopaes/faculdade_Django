from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cadastro_cliente/', views.cadastro, name='cadastro'),
    url(r'^lista_dos_clientes/', views.lista_cliente, name='lista_cliente'),
    url(r'^deletar_cliente/', views.deletar_cliente, name='deletar_cliente'),
	url(r'^editar_cliente/', views.editar_cliente, name='editar_cliente'),
]