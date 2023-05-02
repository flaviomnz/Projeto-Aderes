from django.db import models

class Usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
