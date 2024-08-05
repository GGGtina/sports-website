from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class GameSeason(models.Model):
    game_date = models.DateField(primary_key=True)
    season = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'season'


class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    game_date = models.ForeignKey(GameSeason, models.DO_NOTHING, db_column='game_date')
    team_id_home = models.ForeignKey('Team', models.DO_NOTHING, db_column='team_id_home', related_name='team_id_home')
    wl_home = models.CharField(max_length=1)
    PTS_home = models.IntegerField(db_column='PTS_home')  # Field name made lowercase.
    team_id_away = models.ForeignKey('Team', models.DO_NOTHING, db_column='team_id_away', related_name='team_id_away')
    wl_away = models.CharField(max_length=1)
    PTS_away = models.IntegerField(db_column='PTS_away')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'game'


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=45, default='')
    is_active = models.IntegerField()
    birthday = models.DateField()
    school = models.CharField(max_length=50)
    country = models.CharField(max_length=45)
    height = models.IntegerField()
    weight = models.IntegerField()
    jersey = models.IntegerField()
    position = models.CharField(max_length=45)
    team = models.ForeignKey('Team', models.DO_NOTHING)
    PTS = models.FloatField(db_column='PTS')  # Field name made lowercase.
    AST = models.FloatField(db_column='AST')  # Field name made lowercase.
    REB = models.FloatField(db_column='REB')  # Field name made lowercase.

    # def __str__(self):
    #     if self.player_name:
    #         return self.player_name
    #     else:
    #         return "no_name"

    class Meta:
        managed = False
        db_table = 'player'


class StateCity(models.Model):
    city_name = models.CharField(primary_key=True, max_length=30)
    state = models.CharField(max_length=45)

    # def __str__(self):
    #     if self.city_name:
    #         return self.city_name
    #     else:
    #         return "no_name"

    class Meta:
        managed = False
        db_table = 'state_city'


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    full_name = models.ForeignKey('TeamNickname', models.DO_NOTHING, db_column='full_name', unique=True)
    city = models.ForeignKey(StateCity, models.DO_NOTHING, db_column='city')
    founded_year = models.IntegerField()

    # def __str__(self):
    #     if self.full_name:
    #         return self.full_name
    #     else:
    #         return "no_name"

    class Meta:
        managed = False
        db_table = 'team'


class TeamNickname(models.Model):
    full_name = models.CharField(primary_key=True, max_length=45)
    name = models.CharField(max_length=3)
    nick_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'team_nickname'


class CustomUser(models.Model):
    user = models.CharField(max_length=25, unique=True)
    role = models.CharField(max_length=30)


class InvitationCode(models.Model):
    code = models.CharField(max_length=64, null=False)
    role = models.CharField(max_length=30)


