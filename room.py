import pygame

import lib
import wall

class Room():
    def __init__(self, name: str, background_image: str, collider_mesh: list) -> object:
        self.name = name

        self.active = False

        self.background = pygame.image.load(background_image).convert_alpha()

        self.walls = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.collidables = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

        self.create_walls(collider_mesh)
        print(self.walls)

    def create_walls(self, collider_mesh) -> None:
        for pointArray in range(len(collider_mesh)):
            w = wall.Wall(collider_mesh[pointArray][0], collider_mesh[pointArray][1], collider_mesh[pointArray][2], collider_mesh[pointArray][3])
            self.walls.add(w)
            self.collidables.add(w)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.background, (0, 0))
        self.walls.draw(surface)

    def update(self) -> None:
        self.enemies.update()
        self.collidables.update()
        self.projectiles.update()

class SpawnRoom(Room):
    def __init__(self) -> Room:
        super().__init__("spawn", "assets/tiled/spawn_test.png", collider_mesh["spawn"])

class StandardRoom(Room):
    def __init__(self, name: str, background: str, collider_tag: str) -> Room:
        super().__init__(name, background, collider_mesh[collider_tag])

collider_mesh = {
    "spawn": [
        [5, 5, 10, 1]
    ]
}