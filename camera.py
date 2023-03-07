import pygame

import lib

class PlayerCenterCamera(pygame.sprite.Group):
    def __init__(self, display_surface: pygame.Surface, ground_surface: pygame.Surface) -> pygame.sprite.Group:
        pygame.sprite.Group.__init__(self)

        self.display_surface = display_surface
        self.half_width = int(self.display_surface.get_width() / 2)
        self.half_height = int(self.display_surface.get_height() // 2)

        self.ground_surface = ground_surface
        self.ground_rect = self.ground_surface.get_rect(topleft = (0, 0))

    def center_target_camera(self, target: pygame.sprite.Sprite) -> None:
        lib.global_offset.x = target.rect.centerx - self.half_width
        lib.global_offset.y = target.rect.centery - self.half_height

    def camera_draw(self, player: pygame.sprite.Sprite) -> None:
        self.center_target_camera(player)

        ground_offset = self.ground_rect.topleft - lib.global_offset
        self.display_surface.blit(self.ground_surface, ground_offset)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - lib.global_offset
            self.display_surface.blit(sprite.image, offset_pos)