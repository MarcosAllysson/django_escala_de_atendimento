# Generated by Django 3.2.4 on 2021-07-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escala', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escala',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]