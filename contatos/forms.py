from django import forms
from .models import Contatos

class ContatosForm(forms.ModelForm):

    class Meta:
        model = Contatos
        fields = ('nome', 'email', 'telefone_residencia', 'telefone_celular', 'endereço',)

    def clean(self):

        super(ContatosForm, self).clean()

        nome = self.cleaned_data.get('nome')
        email = self.cleaned_data.get('email')
        telefone_residencia = self.cleaned_data.get('telefone_residencia')
        telefone_celular = self.cleaned_data.get('telefone_celular')
        endereço = self.cleaned_data.get('endereço')

        


        return self.cleaned_data