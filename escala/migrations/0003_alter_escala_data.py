# Generated by Django 3.2.4 on 2021-07-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escala', '0002_alter_escala_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escala',
            name='data',
            field=models.DateField(verbose_name='Data'),
        ),
    ]
