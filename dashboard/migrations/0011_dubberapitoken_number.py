# Generated by Django 4.0 on 2022-01-13 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_dubbersmslogs_smscontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='dubberapitoken',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
