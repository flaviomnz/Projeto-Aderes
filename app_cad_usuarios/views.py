from django.shortcuts import render
from .models import Usuario

# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #Salvando os dados da tela p/ o banco de dados
    novo_usuario = Usuario()
    novo_usuario_name = request.POST.get('name')
    novo_usuario_email = request.POST.get('email')
    novo_usuario.save()


    #Exibindo todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }


    #Retornando os dados para a página de listagem de usuarios.
    return render(request,'usuarios/usuarios.html',usuarios)