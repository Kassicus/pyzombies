import pygame

class PlayerCenterCamera(pygame.sprite.Group):
    def __init__(self, display_surface: pygame.Surface) -> pygame.sprite.Group:
        pygame.sprite.Group.__init__(self)

        self.display_surface = display_surface

    def camera_draw(self) -> None:
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            self.display_surface.blit(sprite.image, sprite.rect.center)