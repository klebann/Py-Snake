import pygame
import settings


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.body = pygame.image.load("resources/head.png").convert_alpha()
        self.x = [settings.SIZE] * length
        self.y = [settings.SIZE] * length
        self.length = length
        self.direction = 'right'

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.body, (self.x[i], self.y[i]))

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def follow(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

    def walk(self):
        self.follow()

        if self.direction == 'up':
            self.y[0] -= settings.SIZE
        if self.direction == 'down':
            self.y[0] += settings.SIZE
        if self.direction == 'left':
            self.x[0] -= settings.SIZE
        if self.direction == 'right':
            self.x[0] += settings.SIZE

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
