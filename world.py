import pygame

import lib
import camera
import player
import room

class World():
    def __init__(self, background_path: str) -> object:
        lib.level_ref = self

        self.display_surface = pygame.display.get_surface()
        self.world_background = pygame.image.load(background_path).convert_alpha()

        lib.world_camera = camera.PlayerCenterCamera(self.display_surface)
        self.player = player.Player()

        lib.world_camera.add(self.player)

        self.rooms = {
            "spawn": room.SpawnRoom()
        }

        self.active_room = self.change_active_room("spawn")
    
    def change_active_room(self, name: str) -> object:
        if name in self.rooms:
            return(self.rooms[name])

    def draw(self) -> None:
        lib.world_camera.camera_draw()

    def update(self) -> None:
        lib.world_camera.update()