import pygame

import lib

class Wall(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__()

        self.color = lib.color.MAGENTA
        self.scale = 32

        self.pos = pygame.math.Vector2(x * self.scale, y * self.scale)

        self.image = pygame.Surface([width * self.scale, height * self.scale])
        self.image.fill(self.color)
        #self.image.set_colorkey(self.color)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos