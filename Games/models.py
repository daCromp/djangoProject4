from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    GAME_GENRES = [
        ('FPS', 'First-person shooter'),
        ('TPS', 'Third-person shooter'),
        ('RPG', 'Role-playing games'),
        ('MOBA', 'Multiplayer online battle arena'),
    ]

    FSK_TYPES = [
        ('0', 'Altersfreigabe ab 0 Jahren'),
        ('6', 'Altersfreigabe ab 6 Jahren'),
        ('12', 'Altersfreigabe ab 12 Jahren'),
        ('16', 'Altersfreigabe ab 16 Jahren'),
        ('18', 'Altersfreigabe ab 18 Jahren'),
    ]

    name = models.CharField(max_length=100)

    beschreibung = models.CharField(max_length=100,
                                    blank=True)

    genre = models.CharField(max_length=10,
                             choices=GAME_GENRES)

    fsk = models.CharField(max_length=2,
                           choices=FSK_TYPES,
                           )

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='users',
                             related_query_name='user',
                             )

    erstellung = models.DateTimeField(default=datetime.now,
                                      blank=True)

    class Meta:
        ordering = ['genre', 'name']
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def get_full_title(self):
        return_string = self.name
        if self.beschreibung:
            return_string = self.name + ': ' + self.beschreibung
        return return_string

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.get_full_title() + ' : ' + self.genre
