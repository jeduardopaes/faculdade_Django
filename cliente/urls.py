from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),

    url(r'^cadastro_cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    url(r'^lista_dos_clientes/', views.lista_cliente, name='lista_cliente'),
    url(r'^deletar_cliente/', views.deletar_cliente, name='deletar_cliente'),
    url(r'^editar_cliente/', views.editar_cliente, name='editar_cliente'),

    url(r'^cadastro_roupa/', views.cadastro_roupa, name='cadastro_roupa'),
    url(r'^lista_roupa/', views.lista_roupa, name='lista_roupa'),
    url(r'^deletar_roupa/', views.deletar_roupa, name='deletar_roupa'),
]
