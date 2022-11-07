from django import forms
from .models import Game


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['name', 'beschreibung', 'genre', 'fsk', 'erstellung']
        widgets = {
            'genre': forms.Select(choices=Game.GAME_GENRES),
            'type': forms.Select(choices=Game.FSK_TYPES),
            'ersteller': forms.HiddenInput(),
        }
