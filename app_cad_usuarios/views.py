from django.shortcuts import render
from .models import Usuario
from django.shortcuts import get_object_or_404
from .forms import UsuarioForm

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

    #Onde as informações vão ser exibidas
    return render(request,'usuarios/usuarios.html',usuarios)




#Deletar usuário
def deletarUser(request, id):
    usuarios = Usuario.objects.get(id=id)
    usuarios.delete()
    return render(request, 'usuarios/home.html')



def updateEdit(request, id):
    usuarios = Usuario.objects.get(pk=id)
    return render(request, 'usuarios/updateEdit.html')

    




     
    