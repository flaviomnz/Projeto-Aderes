from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm


# Formulário do usuário

def user(request):
    if request.method=="POST":
        form=UsuarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = UsuarioForm()
        return render(request, 'usuarios/add.html', {'form':form})
    




#Exibir informações do usuário

def show(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/show.html', {'usuarios': usuarios})
    




# Editar usuário

def edit(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'usuarios/edit.html', {'usuario': usuario})




# Atualizar dados de um usuário

def update(request, id):
    usuarios = Usuario.objects.get(id=id)
    form = UsuarioForm(request.POST, instance = usuarios)
    if form.is_valid():
        form.save()
        return redirect ("/show")
    
    return render(request, 'usuarios/edit.html', {'usuarios': usuarios})


# Deletar usuário

def delete(request,id):
    usuarios = Usuario.objects.get(id=id)
    usuarios.delete()
    return redirect("/show")