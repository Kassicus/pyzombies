import pygame

import lib

class Room():
    def __init__(self, name: str, background_image: str) -> object:
        self.name = name

        self.active = False

        self.background = pygame.image.load(background_image).convert_alpha()

        self.enemies = pygame.sprite.Group()
        self.collidables = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.background, (0, 0))

class SpawnRoom(Room):
    def __init__(self) -> Room:
        super().__init__("spawn", "assets/tiled/spawn_test.png")