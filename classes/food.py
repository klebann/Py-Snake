import pygame
import settings
import random


class Food:
    """Class that represents snake food.
    """

    def __init__(self, parent_screen):
        """Create snake food.

        Args:
            parent_screen (pygame.display): Parent display where food will be displayed.
        """
        self.image = pygame.image.load("resources/heart.png").convert_alpha()
        self.parent_screen = parent_screen
        self.set_position()

    def draw(self):
        """Draw food on the screen
        """
        self.parent_screen.blit(self.image, (self.x, self.y))

    def set_position(self):
        """Set position of food.
        """
        self.x = random.randint(0, 24) * settings.SIZE
        self.y = random.randint(0, 19) * settings.SIZE

    def get_position(self):
        """Get food position

        Returns:
            tuple: Food coordinates.
        """
        return (self.x, self.y)
