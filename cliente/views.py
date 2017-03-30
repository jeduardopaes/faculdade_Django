from django.shortcuts import render
from .models import Cliente

def cadastro(request):
    if request.method =='POST':
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        cep = request.POST.get("cep")
        cpf = request.POST.get("cpf")
        telefone = request.POST.get("telefone")
        Cliente.objects.create(nome = nome ,telefone = telefone ,email = email,cep = cep ,cpf = cpf)
    return render(request, 'cadastro_cliente.html')

def lista_cliente(request):
    return render(request, 'lista_cliente.html')
