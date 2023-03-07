import pygame

import lib

class DebugInterface():
    def __init__(self) -> None:
        self.active = False

        self.font = pygame.font.SysFont("Courier", 16)

        self.offset_padding = 10

        self.t_fps = None
        self.t_mouse = None
        self.t_player = None
        self.t_global = None
        self.t_targetm = None

        self.o_fps = 0
        self.o_mouse = 0
        self.o_player = 0
        self.o_global = 0
        self.o_targetm = 0

        self.display_surface = pygame.display.get_surface()

    def get_fps(self, clock: pygame.time.Clock) -> list [pygame.Surface, int]:
        string = "FPS: " + str(int(clock.get_fps()))
        text = self.font.render(string, True, lib.color.CYAN)

        offset = int(lib.SCREEN_WIDTH - text.get_width() - self.offset_padding)

        return text, offset
    
    def get_mouse(self) -> list [pygame.Surface, int]:
        x, y = pygame.mouse.get_pos()
        
        string = "Mouse: " + str(x) + "," + str(y)
        text = self.font.render(string, True, lib.color.CYAN)

        offset = int(lib.SCREEN_WIDTH - text.get_width() - self.offset_padding)

        return text, offset
    
    def get_player(self, player: pygame.sprite.Sprite) -> list [pygame.Surface, int]:
        string = "Player: " + str(int(player.pos.x)) + "," + str(int(player.pos.y))
        text = self.font.render(string, True, lib.color.CYAN)

        offset = int(lib.SCREEN_WIDTH - text.get_width() - self.offset_padding)

        return text, offset
    
    def get_global_offset(self) -> list [pygame.Surface, int]:
        string = "Global Off: " + str(lib.global_offset.x) + "," + str(lib.global_offset.y)
        text = self.font.render(string, True, lib.color.CYAN)

        offset = int(lib.SCREEN_WIDTH - text.get_width() - self.offset_padding)

        return text, offset

    def get_target_mouse(self) -> list [pygame.Surface, int]:
        x, y = lib.relative_mouse_pos

        string = "Target Mouse: " + str(x) + "," + str(y)
        text = self.font.render(string, True, lib.color.CYAN)

        offset = int(lib.SCREEN_WIDTH - text.get_width() - self.offset_padding)

        return text, offset

    def toggle_active(self) -> None:
        if self.active:
            self.active = False
        else:
            self.active = True

    def draw(self) -> None:
        self.display_surface.blit(self.t_fps, (self.o_fps, 10))
        self.display_surface.blit(self.t_mouse, (self.o_mouse, 30))
        self.display_surface.blit(self.t_player, (self.o_player, 50))
        self.display_surface.blit(self.t_global, (self.o_global, 70))
        self.display_surface.blit(self.t_targetm, (self.o_targetm, 90))

    def update(self, clock: pygame.time.Clock, player: pygame.sprite.Sprite) -> None:
        self.t_fps, self.o_fps = self.get_fps(clock)
        self.t_mouse, self.o_mouse = self.get_mouse()
        self.t_player, self.o_player = self.get_player(player)
        self.t_global, self.o_global = self.get_global_offset()
        self.t_targetm, self.o_targetm = self.get_target_mouse()