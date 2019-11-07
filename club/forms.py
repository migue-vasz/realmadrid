from django import forms
from .models import Partido, Jugador, Rotacion, Goal

class FormPartido(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ('fecha_partido','resultado','marcador','competicion','instancia','temporada')

class FormJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ('dorsal','pais','demarcacion','nombre','pierna_buena','estatura','fecha_nacimiento')

class FormRotacion(forms.ModelForm):
    class Meta:
        model = Rotacion
        fields = ('partido','jugador','alineacion','minutos_jugados','temporada')

class FormGoal(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ('partido','anotador','descripcion','temporada')
