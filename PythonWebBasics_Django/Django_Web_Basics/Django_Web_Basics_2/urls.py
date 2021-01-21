from django.urls import path

from Django_Web_Basics_2.views import index as index_view, UsersListView, GamesListView, something

urlpatterns = [
    path('', index_view),
    path('2/', UsersListView.as_view()),
    path('games/', GamesListView.as_view()),
    path('smth/', something),
]