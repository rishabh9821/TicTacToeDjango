# Generated by Django 4.0.6 on 2022-07-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='room_code',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]