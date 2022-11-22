from django import forms
from .models import Game, Comment


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


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'user': forms.HiddenInput(),
            'game': forms.HiddenInput(),
        }