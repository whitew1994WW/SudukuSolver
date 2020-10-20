import unittest
from sudukusolver import SudukuSolver
from coord import Coord

class SudukuProblems(unittest.TestCase):
    def test_basic_suduku(self):
        coords= [{'x': 1, 'y': 1,'value': 5}, {'x': 5, 'y': 1,'value': 1}, {'x': 9, 'y': 1,'value': 4}, {'x': 1, 'y': 2,'value': 2},
        {'x': 2, 'y': 2,'value': 7}, {'x': 3, 'y': 2,'value': 4}, {'x': 7, 'y': 2,'value': 6}, {'x': 2, 'y': 3,'value': 8},
        {'x': 4, 'y': 3,'value': 9}, {'x': 6, 'y': 3,'value': 4}, {'x': 1, 'y': 4,'value': 8}, {'x': 2, 'y': 4,'value': 1},
        {'x': 4, 'y': 4,'value': 4}, {'x': 5, 'y': 4,'value': 6}, {'x': 7, 'y': 4,'value': 3}, {'x': 9, 'y': 4,'value': 2},
        {'x': 3, 'y': 5,'value': 2}, {'x': 5, 'y': 5,'value': 3}, {'x': 7, 'y': 5,'value': 1}, {'x': 1, 'y': 6,'value': 7},
        {'x': 3, 'y': 6,'value': 6}, {'x': 5, 'y': 6,'value': 9}, {'x': 6, 'y': 6,'value': 1}, {'x': 8, 'y': 6,'value': 5},
        {'x': 9, 'y': 6,'value': 8}, {'x': 4, 'y': 7,'value': 5}, {'x': 6, 'y': 7,'value': 3}, {'x': 8, 'y': 7,'value': 1},
        {'x': 1, 'y': 9,'value': 1}, {'x': 5, 'y': 9,'value': 2}, {'x': 9, 'y': 9,'value': 3}, {'x': 3, 'y': 8,'value': 5},
        {'x': 7, 'y': 8,'value': 9}, {'x': 8, 'y': 8,'value': 2}, {'x': 9, 'y': 8,'value': 7}]
        suduku = SudukuSolver(coords)
        suduku.solve()
        pass


if __name__ == '__main__':
    unittest.main()
