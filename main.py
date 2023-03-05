import pygame

import lib
import debug

pygame.init()

class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode([lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT])
        pygame.display.set_caption("PyZombies")

        self.running = True
        self.clock = pygame.time.Clock()

        lib.events = pygame.event.get()

        self.debug_interface = debug.DebugInterface()

    def run(self) -> None:
        while self.running:
            self.events()
            self.draw()
            self.update()

    def keyboard_events(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False

            if event.key == pygame.K_TAB:
                self.debug_interface.toggle_active()

    def events(self) -> None:
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

            self.keyboard_events(event)

    def draw(self) -> None:
        self.screen.fill(lib.color.BLACK)

        if self.debug_interface.active:
            self.debug_interface.draw()

    def update(self) -> None:

        self.debug_interface.update(self.clock)
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.framerate) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()