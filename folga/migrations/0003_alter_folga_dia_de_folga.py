# Generated by Django 3.2.4 on 2021-07-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folga', '0002_alter_folga_dia_de_folga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folga',
            name='dia_de_folga',
            field=models.DateField(),
        ),
    ]
