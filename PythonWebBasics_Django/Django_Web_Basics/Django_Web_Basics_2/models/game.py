from django.db import models

from Django_Web_Basics_2.models.player import Player


class GameManager(models.Manager):
    def get_all_with_players_count(self):
        return self.all()\
            .annotate(players_count=models.Count('players'))


class Game(models.Model):
    objects = GameManager()
    EASY = 0
    MEDIUM = 1
    HARD = 2

    DIFFICULTY_LEVELS_CHOICES = (
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    )
    name = models.CharField(max_length=30)
    level_of_difficulty = models.IntegerField(
        blank=False,
        choices=DIFFICULTY_LEVELS_CHOICES,
        default=EASY
    )
    players = models.ManyToManyField(Player)

    def __str__(self):
        return f'{self.name}'