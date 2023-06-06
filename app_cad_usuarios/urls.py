from django.urls import path
from app_cad_usuarios import views


#rota, view responsavel e nome para referência (caso necessário)
urlpatterns = [
    path('user', views.user, name="user"),
    path('show', views.show, name="show"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('update/<int:id>/', views.update, name="update"),
]

