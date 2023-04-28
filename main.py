import pygame
from mtv.states.game import Game

game = dict(done=False)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("mtv")

    screen = pygame.display.set_mode((1020, 800))
    clock = pygame.time.Clock()

    surface = pygame.display.get_surface()
    fps = 40

    game = Game()

    while not game.done:
        game.draw(screen)

        events = pygame.event.get()
        game.handle_events(events)

        game.draw(surface)
        pygame.display.flip()

        game.update(clock.tick(fps))
