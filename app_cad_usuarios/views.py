from django.shortcuts import render
from .models import Usuario
from django.shortcuts import get_object_or_404

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



def editar(request, id):
    usuarios = get_object_or_404(Usuario, id=id)
    
    if request.method == 'POST':
        # atualizar os campos do objeto com base nos dados do formulário

        editar_usuario = Usuario()
        editar_usuario.name = request.POST['name']
        editar_usuario.email = request.POST['email']

        usuarios.save()  # Salve as alterações no banco de dados

        # Redirecionamento
        return render(request, 'usuarios/editar')





     
    