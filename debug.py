import pygame

import lib

class DebugInterface():
    def __init__(self) -> None:
        self.active = False

        self.font = pygame.font.SysFont("Courier", 16)

        self.t_fps, self.t_mouse = None, None
        self.o_fps, self.o_mouse = 0, 0

        self.display_surface = pygame.display.get_surface()

    def get_fps(self, clock: pygame.time.Clock) -> list [pygame.Surface, int]:
        string = "FPS: " + str(int(clock.get_fps()))
        text = self.font.render(string, True, lib.color.CYAN)

        offset = int(lib.SCREEN_WIDTH - text.get_width() - 10)

        return text, offset
    
    def get_mouse(self) -> list [pygame.Surface, int]:
        x, y = pygame.mouse.get_pos()
        
        string = "Mouse: " + str(x) + "," + str(y)
        text = self.font.render(string, True, lib.color.CYAN)

        offset = int(lib.SCREEN_WIDTH - text.get_width() - 10)

        return text, offset
    
    def toggle_active(self) -> None:
        if self.active:
            self.active = False
        else:
            self.active = True

    def draw(self) -> None:
        self.display_surface.blit(self.t_fps, (self.o_fps, 10))
        self.display_surface.blit(self.t_mouse, (self.o_mouse, 30))

    def update(self, clock: pygame.time.Clock) -> None:
        self.t_fps, self.o_fps = self.get_fps(clock)
        self.t_mouse, self.o_mouse = self.get_mouse()