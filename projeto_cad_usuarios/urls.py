from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsavel e nome de referência
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
    path('deletarUser/<int:id>', views.deletarUser, name='deletarUser'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
]

