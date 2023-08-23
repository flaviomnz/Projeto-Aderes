from rolepermissions.checkers import has_role_permission
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard_empresa_a(request):
    if has_role_permission(request.user, 'acessar_dashboard_empresa_a'):
        return render(request, 'dashboard_empresa_a.html')
    else:
        # Redirecionar ou mostrar mensagem de erro
        pass

@login_required
def dashboard_empresa_b(request):
    if has_role_permission(request.user, 'acessar_dashboard_empresa_b'):
        return render(request, 'dashboard_empresa_b.html')
    else:
        # Redirecionar ou mostrar mensagem de erro
        pass
