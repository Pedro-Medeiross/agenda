# Generated by Django 3.0.2 on 2020-01-28 03:20

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0017_auto_20200127_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='endereço',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='contatos',
            name='telefone_celular',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+55', max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='contatos',
            name='telefone_residencia',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+55', max_length=128, null=True, region=None),
        ),
    ]
