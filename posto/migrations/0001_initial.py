# Generated by Django 3.2.4 on 2021-07-10 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_posto', models.CharField(max_length=120, verbose_name='Posto')),
                ('endereco', models.CharField(max_length=120, verbose_name='Endereço')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
            ],
            options={
                'verbose_name': 'Posto',
                'verbose_name_plural': 'Postos',
                'ordering': ['nome_do_posto'],
            },
        ),
    ]
