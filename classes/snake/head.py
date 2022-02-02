from re import X
from pygame import image, transform
import settings


class Head:
    """Snake Head class, that manages display, moving and direction of snake
    """

    def __init__(self, parent_screen):
        """Create snake head

        Args:
            parent_screen (pygame.display): Parent screen where snake will be displayed.
        """
        self.parent_screen = parent_screen
        self.image = image.load("resources/head.png").convert_alpha()
        self.direction = 'right'
        self.x, self.y = settings.STARTING_POSITION

    def move(self, x, y):
        """Move snake head position by x and y coordinates.

        Args:
            x (int): X coordinate
            y (int): Y coordinate
        """
        self.x += x * settings.SIZE
        self.y += y * settings.SIZE

    def draw(self, direction):
        """Draw snake head in corect direction.

        Args:
            direction (string): Head position.
        """
        head = self.rotate_head(direction)
        self.parent_screen.blit(head, (self.x, self.y))

    def rotate_head(self, direction):
        """Return image of rotatet snake head before display.

        Args:
            direction (string): Snake head direction

        Returns:
            pygame.image: Snake head image correctly rotated.
        """
        if direction == 'up':
            return self.image
        if direction == 'left':
            return transform.rotate(self.image, 90)
        if direction == 'down':
            return transform.rotate(self.image, 180)
        if direction == 'right':
            return transform.rotate(self.image, 270)

    def get_position(self):
        """Get snake head position

        Returns:
            tuple: Coordinates
        """
        return (self.x, self.y)
