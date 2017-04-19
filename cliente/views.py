# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Cliente,Roupa
from django.db import IntegrityError

#====== CLIENTES =================================================================================

def cadastro_cliente(request):
    if request.method =='POST':
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        cep = request.POST.get("cep")
        cpf = request.POST.get("cpf")
        telefone = request.POST.get("telefone")
        info = {'nome':nome, 'email':email, 'cep':cep, 'cpf':cpf, 'telefone': telefone}
        if nome == "" or email == "" or telefone == "" or cpf == "" or cep == "":
            mensagem = "*Preencha todos os campos!"
            return render(request, 'cadastro_cliente.html', { 'info':info, 'mensagem':mensagem })
        else:
            mensagem = "*Cadastro realizado com sucesso!"
            try:
                Cliente.objects.create(**info)
            except IntegrityError:
                mensagem = "cpf já existe!"
            return render(request, 'cadastro_cliente.html', { 'info':info, 'mensagem':mensagem })
        #return lista_cliente(request)
    return render(request, 'cadastro_cliente.html')

def lista_cliente(request):
    lista_clientes = Cliente.objects.all()
    return render(request, 'lista_cliente.html', {'lista_clientes':lista_clientes})

def deletar_cliente(request):
    id = request.GET.get('cliente_id')
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        Cliente.objects.get(id=id).delete()
        return lista_cliente(request)
    return render(request, 'deletar_cliente.html', {'cliente':cliente})

#======== Desenvolvedor: bernardo =======
def editar_cliente(request):
    id = request.GET.get('cliente_id')
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.nome = request.POST.get("nome")
        cliente.email = request.POST.get("email")
        cliente.cep = request.POST.get("cep")
        cliente.cpf = request.POST.get("cpf")
        cliente.telefone = request.POST.get("telefone") 
        cliente.save()
        return lista_cliente(request)
    return render(request, 'editar_cliente.html', {'cliente':cliente})

def home(request):
	return render(request,'index.html')


#======== Desenvolvedor: bernardo =======
    

#====== ROUPAS =================================================================================
def cadastro_roupa(request):
    if request.method == 'POST':
        quantidade = int(request.POST.get("quantidade"))
        nome = request.POST.get("nome")
        tipo = request.POST.get("tipo")
        cor = request.POST.get("cor")
        descricao = request.POST.get("descricao")
        valor = float(request.POST.get("valor"))
        tamanho = request.POST.get("tamanho")
        info = {'tamanho':tamanho,'nome':nome,'cor':cor,'descricao':descricao,'tipo':tipo,'valor':valor,'situacao':"Disponível"}
        
        while quantidade>0 :
            Roupa.objects.create(**info)
            quantidade -= 1
        
        return render(request,'cadastro_roupa.html',{'info':info})
    return render(request,'cadastro_roupa.html')

def lista_roupa(request):
    lista_roupas = Roupa.objects.all()
    return render(request, 'lista_roupa.html', {'lista_roupas':lista_roupas})

def deletar_roupa(request):
    roupa_id = request.GET.get('roupa_id')
    roupa = Roupa.objects.get(id=roupa_id)
    if request.method == 'POST':
        Roupa.objects.get(id=roupa_id).delete()
        return lista_roupa(request)
    return render(request, 'deletar_roupa.html', {'roupa':roupa})
'''
def editar_roupa(request):
    id = request.GET.get('cliente_id')
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.nome = request.POST.get("nome")
        cliente.email = request.POST.get("email")
        cliente.cep = request.POST.get("cep")
        cliente.cpf = request.POST.get("cpf")
        cliente.telefone = request.POST.get("telefone") 
        cliente.save()
        return lista_cliente(request)
    return render(request, 'editar_cliente.html', {'cliente':cliente})'''

