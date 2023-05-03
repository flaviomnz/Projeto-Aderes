from django.db import models


#Objetos python q representam uma tabela no banco de dados

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
