from pygame import image
from .head import Head
from .body import Body
import settings


class Snake:
    def __init__(self, parent_screen, length):

        self.parent_screen = parent_screen
        self.head = Head(parent_screen)
        self.body = Body(parent_screen, length - 1)
        self.length = length
        self.direction = 'right'

    def draw(self):
        self.head.draw(self.direction)
        if self.length > 1:
            self.body.draw(self.head.get_position())

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def walk(self):
        if self.length > 1:
            self.body.follow(self.head.get_position())

        if self.direction == 'up':
            self.head.move(0, -1)
        if self.direction == 'down':
            self.head.move(0, 1)
        if self.direction == 'left':
            self.head.move(-1, 0)
        if self.direction == 'right':
            self.head.move(1, 0)

    def grow(self):
        self.length += 1
        self.body.grow()

    def get_head_position(self):
        return self.head.get_position()

    def get_body_position(self, i):
        return self.body.get_position(i)
