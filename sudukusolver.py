import pandas as pd
from coord import Coord
import itertools

class SudukuSolver:
    """
    Suduku object class representing the grid of numbers
    coord_list: List of coordinate, value pairs for starting the suduku
        e.g. [{'x': 1, 'y': 2, 'value': 5}, {{'x': 5, 'y': 7, 'value': 5}}]
        Note: The grid starts in the top left corner of the suduku and is 1 indexed
    """
    # Stores ararys of all the possible values for each square in the suduku
    suduku_index = pd.Index([0, 1, 2, 3, 4, 5, 6, 7, 8])
    suduku_columns = pd.Index([0, 1, 2, 3, 4, 5, 6, 7, 8])
    possible_values = pd.DataFrame(index=suduku_index, columns=suduku_columns)
    possible_values.astype(object)
    unresolved_coords = []

    def __init__(self, coord_list):
        self.coords = coord_list
        self.initialize_possible_values()
        self.parse_coord_list()

        # Fill with ones to represent the values that haven't been filled yet
        # self.possißble_values.fillna(value=list(range(1, 10)))

    def parse_coord_list(self):
        for coord in self.coords:
            if coord['value'] not in list(range(1, 10)):
                raise ValueError("Values in suduku grid must be an integer between 1 and 9 inclusive")
            if coord['x'] not in list(range(1, 10)):
                raise ValueError("Coordinates must be between 1 and 9")
            self.possible_values.iloc[coord['x']-1, coord['y']-1] = coord['value']
            self.unresolved_coords.append(Coord(coord['x'], coord['y']))

    def solve(self):
        """
        This processes the new known values by removing the values from the possible_values DF where appropriate
        """
        while len(self.unresolved_coords) > 0:
            coord_to_resolve = self.unresolved_coords.pop(-1)
            self.resolve_column(coord_to_resolve)
            self.resolve_row(coord_to_resolve)
            self.resolve_box(coord_to_resolve)


    def resolve_row(self, coord):
        """ Removes the possible values from other column entries based on the new value inserted """
        coords = [(coord.x_ind, y) for y in list(range(9)) if y != coord.y_ind]
        self.resolve(coord, coords)

    def resolve_column(self, coord):
        """ Removes the possible values from other row entries based on the new value inserted """
        coords = [(x, coord.y_ind) for x in list(range(9)) if x != coord.x_ind]
        self.resolve(coord, coords)

    def resolve_box(self, coord):
        """ Removes the possible values from other entries in the box based on the new value inserted """
        coords = itertools.product(list(range((3*(coord.get_x_box()-1)), 3*coord.get_x_box())),
                                   list(range((3*(coord.get_y_box()-1)), 3*coord.get_y_box())))
        self.resolve(coord, coords)

    def resolve(self, coord, coords):
        """ Removes the value at posotion 'coord' from all of the coordinates in the list coords"""
        for (x, y) in coords:
            if isinstance(self.possible_values.iloc[x, y], list) and \
                    self.possible_values.iloc[coord.x_ind, coord.y_ind] in self.possible_values.iloc[x, y]:
                self.possible_values.iloc[x, y].remove(self.possible_values.iloc[coord.x_ind, coord.y_ind])
            if isinstance(self.possible_values.iloc[x, y], list) and len(self.possible_values.iloc[x, y]) == 1:
                self.unresolved_coords.append(Coord(x + 1, y + 1))
                self.possible_values.iloc[x, y] = self.possible_values.iloc[x, y][0]

    def initialize_possible_values(self):
        for i in self.possible_values.index:
            for col in self.possible_values.columns:
                self.possible_values.loc[i, col] = [1, 2, 3, 4, 5, 6, 7, 8, 9]


