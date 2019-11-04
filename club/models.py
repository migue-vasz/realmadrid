from django.db import models
from django.contrib import admin

class Jugador(models.Model):
    dorsal           = models.IntegerField()
    pais             = models.CharField(max_length=30)
    demarcacion      = models.CharField(max_length=30)
    nombre           = models.CharField(max_length=30)
    pierna_buena     = models.CharField(max_length=30)
    estatura         = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre

class Partido(models.Model):
    fecha_partido = models.DateField()
    resultado     = models.CharField(max_length=30)
    marcador      = models.CharField(max_length=30)
    competicion   = models.CharField(max_length=30)
    instancia     = models.CharField(max_length=50)
    temporada     = models.CharField(max_length=10)
    def __str__(self):
        return self.marcador

class Rotacion(models.Model):
    partido         = models.ForeignKey(Partido, on_delete=models.CASCADE)
    jugador         = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    alineacion      = models.CharField(max_length=30)
    minutos_jugados = models.IntegerField()
    temporada       = models.CharField(max_length=10)

class Goal(models.Model):
    partido     = models.ForeignKey(Partido, on_delete=models.CASCADE)
    anotador    = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    temporada   = models.CharField(max_length=10)

class JugadorAdmin(admin.ModelAdmin):
    inlines = ()

class PartidoAdmin (admin.ModelAdmin):
    inlines = ()

class RotacionAdmin (admin.ModelAdmin):
    inlines = ()

class GoalAdmin (admin.ModelAdmin):
    inlines = ()
