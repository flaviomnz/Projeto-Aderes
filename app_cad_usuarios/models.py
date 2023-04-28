from django.db import models

class Usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255)
    name = models.TextField(max_length=255)
    password = models.CharField(max_length=30)

