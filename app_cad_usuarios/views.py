from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.name = request.POST.get('name')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()

    #Exibindo os usuarios cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #Onde as informações vão ser exibidas
    return render(request,'usuarios/usuarios.html', usuarios)


#DELETAR USUÁRIO
def deletarUser(request, id):
    usuarios = Usuario.objects.get(id=id)
    usuarios.delete()
    return render(request, 'usuarios/home.html')

#EDITAR    
def edit(request, id):
    usuarios = Usuario.objects.get(id=id)
    return render(request, 'usuarios/edit.html', {"usuario": usuarios})


#ATUALIZAR CADASTRO
def update(request, id):
    name = request.POST.get("name")
    email = request.POST.get("email")
    usuarios = Usuario.objects.get(id=id)
    usuarios.name = name
    usuarios.email = email 
    usuarios.save()

    return render(request, 'usuarios/usuarios.html')
    



     
    