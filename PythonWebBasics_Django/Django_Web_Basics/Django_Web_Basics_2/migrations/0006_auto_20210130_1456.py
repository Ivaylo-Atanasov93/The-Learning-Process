# Generated by Django 3.1.5 on 2021-01-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_Web_Basics_2', '0005_game_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='level_of_difficulty',
            field=models.IntegerField(choices=[('Easy', 0), ('Medium', 1), ('Hard', 2)]),
        ),
    ]