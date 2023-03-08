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
            "r1": room.StandardRoom("Room 1", "assets/tiled/r1_test.png", "spawn")
        }

        self.active_room = self.change_active_room("spawn")
    
    def change_active_room(self, name: str) -> object:
        if name in self.rooms:
            return(self.rooms[name])

    def check_collisions(self) -> None:
        collision_tollerance = 3

        for c in self.active_room.walls:
            if self.player.rect.colliderect(c.rect):
                if abs(self.player.rect.left - c.rect.right) < collision_tollerance:
                    self.player.vel.x = 0
                    self.player.pos.x = c.rect.right + self.player.rect.width / 2
                if abs(self.player.rect.right - c.rect.left) < collision_tollerance:
                    self.player.vel.x = 0
                    self.player.pos.x = c.rect.left - self.player.rect.width / 2

                if abs(self.player.rect.top - c.rect.bottom) < collision_tollerance:
                    self.player.vel.y = 0
                    self.player.pos.y = c.rect.bottom + self.player.rect.height / 2
                if abs(self.player.rect.bottom - c.rect.top) < collision_tollerance:
                    self.player.vel.y = 0
                    self.player.pos.y = c.rect.top - self.player.rect.height / 2

    def draw(self) -> None:
        self.active_room.draw(self.display_surface)
        lib.world_camera.camera_draw()

    def update(self) -> None:
        self.active_room.update()
        lib.world_camera.update()
        self.check_collisions()