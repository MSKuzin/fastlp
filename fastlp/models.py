from datetime import datetime

from django.db import models


# Create your models here.


class Player(models.Model):
    nickname = models.CharField(max_length=50, help_text="Player's nickname")
    dota_id = models.CharField(max_length=50, help_text="Player's dota id")
    misc_data = models.TextField("Custom user data", blank=True,
                                 help_text="Put here some information about how to reach this user, e.g. vk, steam, facebook, etc")

    def __str__(self):
        return self.nickname


class Payment(models.Model):
    player = models.ForeignKey(Player)
    number_of_games = models.IntegerField(default=5, help_text="Number of games player has paid for")
    price_of_game = models.CharField(max_length=3, choices=(("USD", "1 USD per game"), ("RUB", "30 RUB per game")),
                                     default="RUB")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {} games, {}, at {}".format(self.player.nickname, str(self.number_of_games), self.price_of_game, datetime.strftime(self.timestamp, "%Y.%m.%d %H:%M"))


class Game(models.Model):
    # this must be changed to user model
    host = models.CharField(max_length=50, help_text="Host of this game")
    players = models.ManyToManyField(Player, help_text="All players in party for this game")
    start_time = models.DateTimeField(help_text="Start time of the game")
    finish_time = models.DateTimeField(help_text="Finish time of the game")

    def __str__(self):
        return "Game " + str(self.id)
