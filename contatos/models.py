from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField



class Contatos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(help_text='example@example.com', max_length=254,null=True, blank=True)
    telefone_residencia = PhoneNumberField(null=True, blank=True, default='+55')
    telefone_celular = PhoneNumberField(null=True, blank=True, default='+55')
    endereço = models.CharField(default="" ,max_length=300, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Contatos'