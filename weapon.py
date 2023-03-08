import pygame

import lib

class BaseWeapon(pygame.sprite.Sprite):
    def __init__(self, player: pygame.sprite.Sprite) -> pygame.sprite.Sprite:
        super().__init__()

        self.player = player

        self.pos = pygame.math.Vector2(self.player.pos.x, self.player.pos.y + 10)

        #TODO: make an actual image for this so we can get clean rotations
        self.image = pygame.Surface([32, 8])
        self.image.fill(lib.color.GREEN)

        self.original_image = self.image

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def rotate(self) -> None:
        _, angle = (lib.relative_mouse_pos-self.pos).as_polar()
        self.image = pygame.transform.rotozoom(self.original_image, -angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self) -> None:
        self.pos.x = self.player.pos.x
        self.pos.y = self.player.pos.y + 10
        self.rect.center = self.pos

        self.rotate()


class StarterHandgun(BaseWeapon):
    def __init__(self, player: pygame.sprite.Sprite) -> BaseWeapon:
        super().__init__(player)