# Generated by Django 3.2.4 on 2021-07-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escala', '0004_alter_escala_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='escala',
            options={'ordering': ['-data'], 'verbose_name': 'Escala', 'verbose_name_plural': 'Escalas'},
        ),
        migrations.AlterField(
            model_name='escala',
            name='data',
            field=models.DateTimeField(help_text='Ex: 01/01/2021'),
        ),
    ]
