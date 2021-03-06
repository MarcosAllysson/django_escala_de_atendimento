# Generated by Django 3.2.4 on 2021-07-10 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medico', '0001_initial'),
        ('posto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.medico')),
                ('posto_de_trabalho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posto.posto')),
            ],
            options={
                'verbose_name': 'Escala',
                'verbose_name_plural': 'Escalas',
                'ordering': ['data'],
            },
        ),
    ]
