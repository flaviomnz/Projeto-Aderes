from django import forms
from django.forms import fields
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields="__all__"