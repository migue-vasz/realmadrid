from django.contrib import admin
from club.models import Jugador, JugadorAdmin, Partido, PartidoAdmin, Rotacion, RotacionAdmin, Goal, GoalAdmin

admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Partido, PartidoAdmin)
admin.site.register(Rotacion, RotacionAdmin)
admin.site.register(Goal, GoalAdmin)
