import pygame

import lib

class Player(pygame.sprite.Sprite):
    def __init__(self) -> pygame.sprite.Sprite:
        super().__init__()

        self.pos = pygame.math.Vector2(lib.SCREEN_WIDTH / 2, lib.SCREEN_WIDTH / 2)
        self.vel = pygame.math.Vector2()

        self.speed = 200

        self.image = pygame.Surface([32, 32])
        self.image.fill(lib.color.BLUE)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def move(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vel.x = -self.speed
        elif keys[pygame.K_d]:
            self.vel.x = self.speed
        else:
            self.vel.x = 0

        if keys[pygame.K_w]:
            self.vel.y = -self.speed
        elif keys[pygame.K_s]:
            self.vel.y = self.speed
        else:
            self.vel.y = 0

    def event_loop(self) -> None:
        pass

    def update(self) -> None:
        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

        self.move()