from re import X
from pygame import image, transform
import settings


class Head:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = image.load("resources/head.png").convert_alpha()
        self.direction = 'right'
        self.x, self.y = settings.STARTING_POSITION

    def move(self, x, y):
        self.x += x * settings.SIZE
        self.y += y * settings.SIZE

    def draw(self, direction):
        head = self.rotate_head(direction)
        self.parent_screen.blit(head, (self.x, self.y))

    def rotate_head(self, direction):
        if direction == 'up':
            return self.image
        if direction == 'left':
            return transform.rotate(self.image, 90)
        if direction == 'down':
            return transform.rotate(self.image, 180)
        if direction == 'right':
            return transform.rotate(self.image, 270)

    def get_position(self):
        return (self.x, self.y)
