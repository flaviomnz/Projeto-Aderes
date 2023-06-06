from django.db import models
from django.core.exceptions import ValidationError


#Objetos python q representam uma tabela no banco de dados

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "%s" %(self.name)
    
class Meta:
    db_table="usuario"