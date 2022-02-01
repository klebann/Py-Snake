from pygame import image, transform
from enum import Enum
import settings


class Type(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    CORNER_UP_LEFT = 3
    CORNER_UP_RIGHT = 4
    CORNER_DOWN_RIGHT = 5
    CORNER_DOWN_LEFT = 6


class Body_Tile:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x, self.y = (-settings.SIZE, -settings.SIZE)
        self.type = Type.HORIZONTAL

    def draw(self):
        image = self.get_image()
        self.parent_screen.blit(image, (self.x, self.y))

    def get_image(self):
        body = image.load("resources/body.png").convert_alpha()
        if self.type == Type.HORIZONTAL:
            return body
        if self.type == Type.VERTICAL:
            return transform.rotate(body, 90)

        corner = image.load("resources/body_corner.png").convert_alpha()
        if self.type == Type.CORNER_UP_LEFT:
            return transform.rotate(corner, 270)
        if self.type == Type.CORNER_UP_RIGHT:
            return transform.rotate(corner, 180)
        if self.type == Type.CORNER_DOWN_RIGHT:
            return transform.rotate(corner, 90)
        if self.type == Type.CORNER_DOWN_LEFT:
            return corner

    def set_position(self, position):
        self.x, self.y = position

    def get_position(self):
        return (self.x, self.y)
