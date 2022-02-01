import pygame
import settings
import random


class Food:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/heart.png").convert_alpha()
        self.parent_screen = parent_screen
        self.set_position()

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def set_position(self):
        self.x = random.randint(0, 24) * settings.SIZE
        self.y = random.randint(0, 19) * settings.SIZE

    def get_position(self):
        return (self.x, self.y)
