class Coord:
    """
    Class to represent suduku coordinates, and to fetch the 'box' number for the subgrids and suduku multi index
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_ind = x - 1
        self.y_ind = y - 1

    def get_x_box(self):
        return (self.x+2) // 3

    def get_y_box(self):
        return (self.y+2) // 3

    def __eq__(self, other):
        if not isinstance(other, Coord):
            return ValueError("Can only compare Coords to Coords")
        if (other.x == self.x) and (other.y == self.y):
            return True
        else:
            return False

    def __str__(self):
        return "X: {}, Y: {}".format(self.x, self.y)
