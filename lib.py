import pygame
import random

UNIT_SIZE = 32

WIDTH_UNITS = 40
HEIGHT_UNITS = 30

SCREEN_WIDTH = int(WIDTH_UNITS * UNIT_SIZE)
SCREEN_HEIGHT = int(HEIGHT_UNITS * UNIT_SIZE)

class Color():
    def __init__(self) -> None:
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)
        self.RED = pygame.Color(255, 0, 0, 255)
        self.GREEN = pygame.Color(0, 255, 0, 255)
        self.BLUE = pygame.Color(0, 0, 255, 255)
        self.YELLOW = pygame.Color(255, 255, 0, 255)
        self.MAGENTA = pygame.Color(255, 0, 255, 255)
        self.CYAN = pygame.Color(0, 255, 255, 255)

    def get_random(self) -> pygame.Color:
        c = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return c
    
color = Color()

events = None

delta_time = 0
framerate = 120

global_offset = pygame.math.Vector2()
level_ref = None