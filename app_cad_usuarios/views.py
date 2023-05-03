from django.shortcuts import render
from .models import Usuario

# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #Salvando os dados da tela p/ o banco de dados
    novo_usuario = Usuario()

    novo_usuario.name = request.POST.get('name')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()


    #Exibindo os usuarios cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #onde as informações vão ser exibidas
    return render(request,'usuarios/usuarios.html',usuarios)