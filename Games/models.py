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

    def get_upvotes(self):
        upvotes = Vote.objects.filter(up_or_down='U',
                                      game=self)
        return upvotes

    def get_upvotes_count(self):
        return len(self.get_upvotes())

    def get_downvotes(self):
        downvotes = Vote.objects.filter(up_or_down='D',
                                        game=self)
        return downvotes

    def get_downvotes_count(self):
        return len(self.get_downvotes())

    def vote(self, user, up_or_down):
        U_or_D = 'U'
        if up_or_down == 'down':
            U_or_D = 'D'
        vote = Vote.objects.create(up_or_down=U_or_D,
                                   user=user,
                                   game=self
                                   )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.get_full_title() + ' : ' + self.genre


class Comment(models.Model):
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def get_comment_prefix(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text

    def get_upvotes(self):
        upvotes = Vote.objects.filter(up_or_down='U',
                                      comment=self)
        return upvotes

    def get_upvotes_count(self):
        return len(self.get_upvotes())

    def get_downvotes(self):
        downvotes = Vote.objects.filter(up_or_down='D',
                                        comment=self)
        return downvotes

    def get_downvotes_count(self):
        return len(self.get_downvotes())

    def vote(self, user, up_or_down):
        # Jojo: ich muss hier Object.filter(user, comment-> down/up) aufrufen

        U_or_D = 'U'
        if up_or_down == 'down':
            U_or_D = 'D'
        vote = Vote.objects.create(up_or_down=U_or_D,
                                   user=user,
                                   comment=self
                                   )
    def __str__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ')'

    def __repr__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ' / ' + str(self.timestamp) + ')'


class Vote(models.Model):
    VOTE_TYPES = [
        ('U', 'up'),
        ('D', 'down'),
    ]

    up_or_down = models.CharField(max_length=1,
                                  choices=VOTE_TYPES,
                                 )
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.up_or_down + ' on ' + self.game.title + ' by ' + self.user.username