from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

from Django_Web_Basics_2.models import Game


def something(request):
    return HttpResponse("<u>It works!</>")


def index(request):
    title = 'Softuni Django101'
    users = User.objects.all()
    context = {
        'title': title,
        'users': users,
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

