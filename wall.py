import pygame

import lib

class Wall(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__()

        self.scale = 32

        self.pos = pygame.math.Vector2(x * self.scale, y * self.scale)
        self.image = pygame.Surface([width * self.scale, height * self.scale])
        self.image.fill(lib.color.BLUE)
        #self.image.set_colorkey(lib.color.BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos