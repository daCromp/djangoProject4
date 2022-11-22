import json

from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from .forms import GameForm, CommentForm
from .models import Game, Comment


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


class GameDeleteView(DeleteView):
    model = Game
    template_name = 'game-delete.html'
    success_url = reverse_lazy("game-list")


def game_list(request):
    all_the_games_in_my_function_based_view = Game.objects.all()
    context = {'all_the_games': all_the_games_in_my_function_based_view}
    return render(request, 'game-list.html', context)


def game_detail(request, **kwargs):
    game_id = kwargs['pk']
    game = Game.objects.get(id=game_id)

    # Add comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.instance.user = request.user
        form.instance.game = game
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    comments = Comment.objects.filter(game=game)
    context = {'that_one_game': game,
               'comments_for_that_one_game': comments,
               'upvotes': game.get_upvotes_count(),
               'downvotes': game.get_downvotes_count(),
               'comment_form': CommentForm}
    return render(request, 'game-detail.html', context)


def game_create(request):
    if request.method == 'POST':
        print("I am in POST")
        form_in_my_function_based_view = GameForm(request.POST)
        form_in_my_function_based_view.instance.user = request.user
        if form_in_my_function_based_view.is_valid():
            form_in_my_function_based_view.save()
            print("I saved new game")
        else:
            pass
            print(form_in_my_function_based_view.errors)

        return redirect('game-list')

    else:  # request.method == 'GET'
        print("I am in GET")
        form_in_my_function_based_view = GameForm()
        context = {'form': form_in_my_function_based_view}
        return render(request, 'game-create-new.html', context)


def game_vote(request, pk: str, up_or_down: str):
    game = Game.objects.get(id=int(pk))
    user = request.user
    game.vote(user, up_or_down)
    return redirect('game-detail', pk=pk)


def comment_vote(request, fk: str, pk: str, up_or_down: str):
    comment = Comment.objects.get(id=int(pk))
    user = request.user
    comment.voteComment(user, up_or_down)
    return redirect('game-detail', pk=fk)


def game_delete(request, id):
    data = get_object_or_404(Game, id=id)
    if request.method == "POST":
        data.delete()
        return redirect("game-list")
    deleteForm = GameForm()
    context = {'form': deleteForm}
    return render(request, "game-delete.html", context)


