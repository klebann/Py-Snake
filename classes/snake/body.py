from pygame import image
from .body_tile import Body_Tile, Type


class Body:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.length = length
        self.tiles = [Body_Tile(parent_screen) for i in range(length)]
        self.lastposition = self.tiles[length-1].get_position()

    def draw(self, head_position):
        self.check_types(head_position)

        for i in range(0, self.length):
            self.tiles[i].draw()

    def check_types(self, head_position):
        for i in range(0, self.length):

            # First body element
            if i == 0:
                previous_x, previous_y = head_position
            else:
                previous_x, previous_y = self.tiles[i-1].get_position()

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
        self.length += 1
        self.tiles.append(Body_Tile(self.parent_screen))

    def follow(self, head_position):
        self.lastposition = self.tiles[self.length - 1].get_position()
        for i in range(self.length - 1, 0, -1):
            self.tiles[i].set_position(self.tiles[i-1].get_position())
        self.tiles[0].set_position(head_position)

    def get_position(self, i):
        return self.tiles[i].get_position()
