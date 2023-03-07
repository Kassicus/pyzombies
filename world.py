import pygame

import lib
import camera
import player

class World():
    def __init__(self, background_path: str) -> object:
        lib.level_ref = self

        self.display_surface = pygame.display.get_surface()
        self.world_background = pygame.image.load(background_path).convert_alpha()

        self.world_camera = camera.PlayerCenterCamera(self.display_surface, self.world_background)
        self.player = player.Player()

        self.world_camera.add(self.player)

    def get_relative_mouse_pos(self) -> pygame.math.Vector2:
        x, y = pygame.mouse.get_pos()

        x += lib.global_offset.x
        y += lib.global_offset.y

        return pygame.math.Vector2(x, y)

    def draw(self) -> None:
        self.world_camera.camera_draw(self.player)

    def update(self) -> None:
        self.world_camera.update()

        lib.relative_mouse_pos = self.get_relative_mouse_pos()