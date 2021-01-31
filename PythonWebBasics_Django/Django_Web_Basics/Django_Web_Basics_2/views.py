from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from Django_Web_Basics_2.models.game import Game
from Django_Web_Basics_2.models.person import Person
from Django_Web_Basics_2.models.player import Player

def something(request):
    return HttpResponse("<u>It works!</>")


def index(request):
    title = 'Softuni Django101'
    users = User.objects.all()
    games = Game.objects.get_all_with_players_count()

    context = {
        'title': title,
        'users': users,
        'games': games
        # 'users': [],
    }
    return render(request, 'index.html', context)


class UsersListView(ListView):
    model = User
    template_name = 'index2.html'
    queryset = User.objects.all().order_by('-username')

    def get_context_object_name(self, object_list):
        return 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'From class View'
        return context


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'


def methods_demo(request):
    context = {
        'name': 'Ivaylo',
        'age': 27,
    }
    if request.content_type == 'application/json':
        return JsonResponse(context)
    return render(request, 'methods_demo.html', context)

def raises_exception(request):
    raise Exception('Raises')

def create_game(request):
    game = Game(
        name='LoL',
        level_of_difficulty=Game.HARD,
    )
    game.save()
    return redirect(request, '')