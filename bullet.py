import pygame
import math

import lib

class BaseBullet(pygame.sprite.Sprite):
    def __init__(self, spawn_x: int, spawn_y: int, target_x: int, target_y: int, speed: float, damage: int, size: int) -> pygame.sprite.Sprite:
        super().__init__()

        self.pos = pygame.math.Vector2(spawn_x, spawn_y)
        self.vel = pygame.math.Vector2()

        self.target_pos = pygame.math.Vector2(target_x, target_y)

        self.speed = speed
        self.damage = damage

        self.image = pygame.Surface([size, size])
        self.image.fill(lib.color.MAGENTA)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.vel = self.get_vectors()

    def get_vectors(self) -> list:
        distance = [self.target_pos.x - self.pos.x, self.target_pos.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        rate = [distance[0] / normal, distance[1] / normal]
        vectors = pygame.math.Vector2(rate[0] * self.speed, rate[1] * self.speed)

        return vectors

    def update(self) -> None:
        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

class NineMil(BaseBullet):
    def __init__(self, spawn_x: int, spawn_y: int, target_x: int, target_y: int) -> BaseBullet:
        super().__init__(spawn_x, spawn_y, target_x, target_y, 100, 1, 5)