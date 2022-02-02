from pygame import image, transform
from enum import Enum
import settings


class Type(Enum):
    """Enum for body tile type

    Args:
        Enum: Enum class
    """
    HORIZONTAL = 1
    VERTICAL = 2
    CORNER_UP_LEFT = 3
    CORNER_UP_RIGHT = 4
    CORNER_DOWN_RIGHT = 5
    CORNER_DOWN_LEFT = 6


class Body_Tile:
    """
    Body tile class that is a part of snake/Body class
    """

    def __init__(self, parent_screen, position=(-settings.SIZE, settings.SIZE)):
        """Initialize new body tile.

        Args:
            parent_screen (pygame.display): Screen where body parts will be displayed.
            position (tuple, optional): Position of new body tile. Defaults to (-settings.SIZE, settings.SIZE).
        """
        self.parent_screen = parent_screen
        self.x, self.y = position
        self.type = Type.HORIZONTAL

    def draw(self):
        """Function to draw body tile on screen
        """
        image = self.get_image()
        self.parent_screen.blit(image, (self.x, self.y))

    def get_image(self):
        """Load graphic for body_tile depending of its type.

        Returns:
            pygame.image: Pygame image class with tile graphic
        """
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
        """Set position of this tile.

        Args:
            position (tuple): New coordinates for this body tile.
        """
        self.x, self.y = position

    def get_position(self):
        """Get position of this tile.

        Returns:
            tuple: Position of this tile.
        """
        return (self.x, self.y)
