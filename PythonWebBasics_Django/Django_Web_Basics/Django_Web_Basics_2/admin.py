from django.contrib import admin

# Register your models here.
from Django_Web_Basics_2.models.game import Game
from Django_Web_Basics_2.models.person import Person
from Django_Web_Basics_2.models.player import Player


class GameAdmin(admin.ModelAdmin):
    filter_horizontal = ('players',)


admin.site.register(Game, GameAdmin)
admin.site.register(Player)
admin.site.register(Person)