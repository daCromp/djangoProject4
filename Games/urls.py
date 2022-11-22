from django.urls import path
from . import views


urlpatterns = [
    path('show/', views.game_list, name='game-list'),
    path('show/<int:pk>/', views.game_detail, name='game-detail'),
    path('show/<int:pk>/vote/<str:up_or_down>/', views.game_vote, name='game_vote'),
    path('add/', views.game_create, name='game-create-new'),
    path('show/<id>/delete', views.game_delete, name='game-delete'),
]