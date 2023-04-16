import pygame
from pygame.locals import Color

from mtv.defs.game import Game
from mtv.domain import player_domain
from mtv.domain import platform_domain
from mtv.domain.controls import handle_key_down_event, handle_key_up_event


def run_game(game: Game) -> None:
    while not game.done:
        handle_events(game)
        update_game(game)
        draw_game(game)
        game.clock.tick(game.fps_max)


def draw_game(game: Game) -> None:
    game.screen.fill(Color("gray20"))
    player_domain.draw_player(game.player)
    platform_domain.draw_platforms(game.platforms)
    pygame.display.flip()


def update_game(game: Game) -> None:
    player_domain.update_player(game.player)


def handle_events(game: Game) -> None:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            game.done = True

        elif event.type == pygame.KEYDOWN:
            handle_key_down_event(game, event)

        elif event.type == pygame.KEYUP:
            handle_key_up_event(game, event)
