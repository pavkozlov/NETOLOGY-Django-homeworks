from django.contrib import admin
from .models import PlayerGameInfo, Player, Game


class PlayerAdmin(admin.ModelAdmin):
    pass


class GameAdmin(admin.ModelAdmin):
    pass


class PlayerGameInfoAmdin(admin.ModelAdmin):
    pass


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(PlayerGameInfo, PlayerGameInfoAmdin)
