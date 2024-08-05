import xadmin
from dataweb.models import Game, GameSeason, Player, StateCity, Team, CustomUser, InvitationCode


class GameAdmin(object):
    list_display = ["game_date", "team_id_home", "wl_home", "PTS_home", "team_id_away", "wl_away", "PTS_away"]


class GameSeasonAdmin(object):
    list_display = ["game_date", "season"]


class PlayerAdmin(object):
    list_display = ["player_name", "is_active", "birthday", "school", "country", "height", "weight", "jersey",
                    "position", "team", "PTS", "AST", "REB"]


class StateCityAdmin(object):
    list_display = ["city_name", "state"]


class TeamAdmin(object):
    list_display = ["full_name",  "city", "founded_year"]


class CustomUserAdmin(object):
    list_display = ["user", "role"]


class InvitationCodeAdmin(object):
    list_display = ["code", "role"]


xadmin.site.register(Game, GameAdmin)
xadmin.site.register(GameSeason, GameSeasonAdmin)
xadmin.site.register(Player, PlayerAdmin)
xadmin.site.register(StateCity, StateCityAdmin)
xadmin.site.register(Team, TeamAdmin)
xadmin.site.register(CustomUser, CustomUserAdmin)
xadmin.site.register(InvitationCode, InvitationCodeAdmin)
