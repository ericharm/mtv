import pygame
from pygame.event import Event
from troid.defs.direction import Direction
from troid.defs.game import Game
from troid.domain import player_domain


def handle_key_down_event(game: Game, event: Event):
    if event.key == pygame.K_ESCAPE:
        game.done = True
    elif event.key == pygame.K_SPACE:
        player_domain.make_player_jump(game.player)
    elif event.key == pygame.K_LEFT:
        game.left_is_pressed = True
        player_domain.make_player_run(game.player, Direction.left)
    elif event.key == pygame.K_RIGHT:
        game.right_is_pressed = True
        player_domain.make_player_run(game.player, Direction.right)


def handle_key_up_event(game: Game, event: Event):
    if event.key == pygame.K_SPACE:
        player_domain.stop_player_jumping(game.player)
    elif event.key == pygame.K_LEFT:
        game.left_is_pressed = False
    elif event.key == pygame.K_RIGHT:
        game.right_is_pressed = False

    if not game.left_is_pressed and not game.right_is_pressed:
        player_domain.stop_player_running(game.player)
