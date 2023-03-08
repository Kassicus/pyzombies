import pygame

import lib
import camera
import player
import room

class World():
    def __init__(self, surface: pygame.Surface) -> object:
        lib.level_ref = self

        self.display_surface = surface

        lib.world_camera = camera.PlayerCenterCamera(self.display_surface)
        self.player = player.Player()

        lib.world_camera.add(self.player)

        self.rooms = {
            "spawn": room.SpawnRoom(),
            "r1": room.StandardRoom("Room 1", "assets/tiled/r1_test.png")
        }

        self.active_room = self.change_active_room("spawn")
    
    def change_active_room(self, name: str) -> object:
        if name in self.rooms:
            return(self.rooms[name])

    def draw(self) -> None:
        self.active_room.draw(self.display_surface)
        lib.world_camera.camera_draw()

    def update(self) -> None:
        self.active_room.update()
        lib.world_camera.update()