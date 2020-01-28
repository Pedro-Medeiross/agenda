from django import forms
from .models import Contatos

class ContatosForm(forms.ModelForm):

    class Meta:
        model = Contatos
        fields = ('nome', 'email', 'telefone_residencia', 'telefone_celular', 'endereço',)