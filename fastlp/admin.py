from django.contrib import admin

from .models import Player, Payment, Game

# Register your models here.

admin.site.register(Player)
admin.site.register(Payment)
admin.site.register(Game)