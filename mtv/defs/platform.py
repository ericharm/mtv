import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface

FILL_COLOR = (0, 255, 255)

class Platform(Sprite):


    def __init__(self, width, height, x, y) -> None:
        Sprite.__init__(self)
        self.image = Surface([width, height])
        self.image.fill(FILL_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = pygame.display.get_surface()

        # self.rect.midbottom = self.screen.get_rect().midbottom

    def draw(self):
        # pygame.draw.rect(screen, (255, 0, 0), self.rect)
        self.screen.blit(self.image, self.rect)

    def collides_with(self, player):
        return self.rect.colliderect(player.rect)

