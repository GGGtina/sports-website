# urls.py file
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('home/', views.home),
    path('search/', views.search),
    path('player_detail/', views.player_detail),
    path('team_detail/', views.team_detail),
    path('game_detail/', views.game_detail),
    path('siteInfo/', views.siteInfo),
    path('manyTeams/', views.manyTeams)
]
