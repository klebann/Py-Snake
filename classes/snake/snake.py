from pygame import image
from .head import Head
from .body import Body
import settings


class Snake:
    """Snake class that manage its head and body.
    """

    def __init__(self, parent_screen, length):
        """Create new snake

        Args:
            parent_screen (pygame.display): Parent screen where snake will be displayed.
            length (int): Snake length
        """
        self.parent_screen = parent_screen
        self.head = Head(parent_screen)
        self.body = Body(parent_screen, length - 1)
        self.length = length
        self.direction = 'right'

    def draw(self):
        """Draw snake head and body
        """
        self.head.draw(self.direction)
        if self.length > 1:
            self.body.draw(self.head.get_position())

    def move_up(self):
        """Set snake direction to up
        """
        if self.direction != 'down':
            self.direction = 'up'

    def move_down(self):
        """Set snake direction to down
        """
        if self.direction != 'up':
            self.direction = 'down'

    def move_left(self):
        """Set snake direction to left
        """
        if self.direction != 'right':
            self.direction = 'left'

    def move_right(self):
        """Set snake direction to right
        """
        if self.direction != 'left':
            self.direction = 'right'

    def walk(self):
        """Move snake body and head
        """
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
        """Snake will grow. Append its length and add new body_tile
        """
        self.length += 1
        self.body.grow()

    def get_head_position(self):
        """Get snake head position

        Returns:
            tuple: Position of snake's head.
        """
        return self.head.get_position()

    def get_body_position(self, i):
        """Get position of i-th body_tile

        Args:
            i (int): Body_Tile index

        Returns:
            tuple: i-th Body Tile
        """
        return self.body.get_position(i)
