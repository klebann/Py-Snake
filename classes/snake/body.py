from pygame import image

import settings
from .body_tile import Body_Tile, Type


class Body:
    """
    Body class that contains Body_tile elements

    Functionality:
     * Manage all Body_Tiles
     * Display Body_Tiles
     * Check type of each Body_Tile
     * Append snake by new Body_Tile
     * Update position of every Body_Tile
    """

    def __init__(self, parent_screen, length):
        """Create new Body class

        Args:
            parent_screen (pygame.display): Parent display
            length (int): How many body parts
        """
        self.parent_screen = parent_screen
        self.length = length
        self.tiles = [Body_Tile(parent_screen) for i in range(length)]
        self.lastposition = self.tiles[length-1].get_position()

    def draw(self, head_position):
        """Draw all Body_Tiles.
        This function also check type of each Body_Tile before drawing.

        Args:
            head_position (tuple): Position of Head element.
        """
        self.check_types(head_position)

        for i in range(0, self.length):
            self.tiles[i].draw()

    def check_types(self, head_position):
        """This function assign type for every Body_Tile depending on position of previous, actual and next tile.

        Args:
            head_position (tuple): Position of Head element.
        """
        for i in range(0, self.length):

            # First body element
            if i == 0:
                previous_x, previous_y = head_position
            else:
                previous_x, previous_y = self.tiles[i-1].get_position()

            # actual tile position
            actual_x, actual_y = self.tiles[i].get_position()

            # Last body element
            if i == self.length - 1:
                next_x, next_y = self.lastposition
            else:
                next_x, next_y = self.tiles[i+1].get_position()

            if previous_x == actual_x == next_x:
                self.tiles[i].type = Type.HORIZONTAL
            elif previous_y == actual_y == next_y:
                self.tiles[i].type = Type.VERTICAL
            elif ((actual_y > previous_y) and (actual_x > next_x)) or ((actual_x > previous_x) and (actual_y > next_y)):
                self.tiles[i].type = Type.CORNER_DOWN_RIGHT
            elif ((actual_y > previous_y) and (actual_x < next_x)) or ((actual_x < previous_x) and (actual_y > next_y)):
                self.tiles[i].type = Type.CORNER_DOWN_LEFT
            elif ((actual_x < previous_x) and (actual_y < next_y)) or ((actual_y < previous_y) and (actual_x < next_x)):
                self.tiles[i].type = Type.CORNER_UP_LEFT
            elif ((actual_x > previous_x) and (actual_y < next_y)) or ((actual_y < previous_y) and (actual_x > next_x)):
                self.tiles[i].type = Type.CORNER_UP_RIGHT

    def grow(self):
        """Add new Body_Tile to snake,
        increase length of body,
        set position and type of new body tile.
        """
        last = self.length-1
        x, y = self.lastposition
        type = self.tiles[last].type
        if (type == Type.HORIZONTAL):
            new_position = (x, -settings.SIZE)
        else:
            new_position = (-settings.SIZE, y)

        body_tile = Body_Tile(self.parent_screen, new_position)

        self.length += 1
        self.tiles.append(body_tile)

    def follow(self, head_position):
        """Set new position of each Body_Tile for new head_position

        Args:
            head_position (tuple): Actual head position
        """
        self.lastposition = self.tiles[self.length - 1].get_position()
        for i in range(self.length - 1, 0, -1):
            self.tiles[i].set_position(self.tiles[i-1].get_position())
        self.tiles[0].set_position(head_position)

    def get_position(self, i):
        """Get postion of i Body_Tile

        Args:
            i (int): index of Body_Tile

        Returns:
            tuple: Position of Body_Tile[i]
        """
        return self.tiles[i].get_position()
