# Generated by Django 3.0.2 on 2020-01-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0012_auto_20200121_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='endereço',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='contatos',
            name='telefone_celular',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='contatos',
            name='telefone_residencia',
            field=models.CharField(max_length=11),
        ),
    ]