import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect  # add import with HttpResonseRedirect
from django.shortcuts import render

from .form import LoginForm, RegisterForm
from .models import CustomUser, Player, Team, Game
from .utils import admin_only


def index(request):
    today = datetime.datetime.now().date()
    return render(request, "hello.html", {"today": today})


def register(request):
    if request.method == 'POST':

        message = ''
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            passwd = form.cleaned_data.get("password")

            code_role = form.cleaned_data.get("invitation_code")
            user = User.objects.create_user(username=username, password=passwd)
            CustomUser.objects.create(user=user, role=code_role)
            return HttpResponseRedirect('/dataweb/login/')
        else:
            return render(request, 'register.html', {'form': form, 'message': message})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            passwd = form.cleaned_data.get("password")
            try:
                user = auth.authenticate(request, username=username, password=passwd)
                if user:
                    auth.login(request, user)
                    if user.is_superuser or user.profile.role == "admin":
                        return HttpResponseRedirect("/admin/")
                    else:
                        return HttpResponseRedirect("/dataweb/home/")
                else:
                    message = 'Incorrect Password or Username!'
            except:
                message = 'Log in success!'
            return render(request, 'login.html', {'form': form, 'message': message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def search(request):
    return render(request, 'search.html')


# add the following two views
def home(request):
    return render(request, 'base.html')


@admin_only
@login_required(login_url="/dataweb/login/")
def player_detail(request):
    page = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 10)
    start = (int(page) - 1) * int(page_size)
    end = start + page_size

    player_name = request.GET.get("player_name")
    players = Player.objects.filter(player_name__icontains=player_name)[start:end]
    return render(request, "player_detail.html", {"players": players})


@login_required(login_url="/dataweb/login/")
def team_detail(request):
    page = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 10)
    start = (int(page) - 1) * int(page_size)
    end = start + page_size

    team_name = request.GET.get("team_name")
    teams = Team.objects.filter(full_name__full_name__icontains=team_name)[start:end].values("team_id",
                                                                                             "full_name",
                                                                                             "full_name__name",
                                                                                             "city__city_name",
                                                                                             "founded_year")
    return render(request, "team_detail.html", {"teams": teams})



@admin_only
@login_required(login_url="/dataweb/login/")
def game_detail(request):
    page = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 10)
    start = (int(page) - 1) * int(page_size)
    end = start + page_size

    team_name = request.GET.get("team_name")
    teams = Team.objects.filter(full_name__name__icontains=team_name).first()
    games = []
    if teams:
        try:
            for i in teams:
                games = Game.objects.filter(team_id_home=i.name)[start:end].values(
                    "game_id", "game_date", "team_id_home__full_name__name", "wl_home",
                    "PTS_home", "team_id_away__full_name__name", "wl_away", "PTS_away")
        except:
            pass
    return render(request, "game_detail.html", {"games": games})


def siteInfo(request):
    return render(request, 'siteInfo.html')


def manyTeams(request):
    return render(request, 'manyTeams.html')


# @admin_only
# @login_required(login_url="/dataweb/login/")
# def game_detail(request):
#     page = request.GET.get("page", 1)
#     page_size = request.GET.get("page_size", 10)
#     start = (int(page) - 1) * int(page_size)
#     end = start + page_size
#
#     team_name = request.GET.get("team_name")
#     home_game = Game.objects.filter(team_id_home__full_name__icontains=team_name)
#     away_game = Game.objects.filter(team_id_away__full_name__icontains=team_name)
#     # games = []
#     if home_game:
#         # game = home_game
#         games = home_game[start:end].values("game_id", "game_date", "team_id_home__full_name__name", "wl_home", "pts_home",
#                                        "team_id_away__full_name__name", "wl_away", "pts_away")
#
#     elif away_game:
#         # game = away_game
#         games = away_game[start:end](team_id_home__full_name__icontains=team_name)[start:end].values("game_id", "game_date", "team_id_home__full_name__name", "wl_home", "pts_home",
#                                        "team_id_away__full_name__name", "wl_away", "pts_away")
#
#     return render(request, "game_detail.html", {"games": games})

# @admin_only
# @login_required(login_url="/dataweb/login/")
# def game_detail(request):
#     page = request.GET.get("page", 1)
#     page_size = request.GET.get("page_size", 10)
#     start = (int(page) - 1) * int(page_size)
#     end = start + page_size
#
#     team_name = request.GET.get("team_name")
#     teams = Team.objects.filter(full_name__name=team_name).first()
#     games = []
#     if teams:
#         home_game = teams.home_game.all()
#         away_game = teams.away_game.all()
#         game = home_game | away_game
#         games = game[start:end].values("game_id", "game_date", "team_id_home__full_name__name", "wl_home", "pts_home",
#                                        "team_id_away__full_name__name", "wl_away", "pts_away")
#
#     return render(request, "game_detail.html", {"games": games})
