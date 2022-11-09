from django import forms
from .models import Game


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['name', 'beschreibung','genre', 'fsk']
        widgets = {
            'genre': forms.Select(choices=Game.GAME_GENRES),
            'fsk': forms.Select(choices=Game.FSK_TYPES),
            'user': forms.HiddenInput(),
            'erstellung': forms.HiddenInput(),
        }
