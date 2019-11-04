from django import forms
from .models import Partido

class FormPartido(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ('fecha_partido','resultado','marcador','competicion','instancia','temporada')
