from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .forms import GameForm
from .models import Game


class GameListView(ListView):
    model = Game
    context_object_name = 'all_the_games'  # Default: object_list
    template_name = 'game-list.html'  # Default: book_list.html


class GameDetailView(DetailView):
    model = Game
    context_object_name = 'that_one_game'  # Default: book
    template_name = 'game-detail.html'  # Default: book_detail.html


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'game-create.html'  # Default: book_form.html
    success_url = reverse_lazy('game-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

