import unittest
from coord import Coord

class TestCoord(unittest.TestCase):
    def test_coord(self):
        coord = Coord(9, 9)
        self.assertEqual(coord.get_x_box(), 3)
        self.assertEqual(coord.get_y_box(), 3)


if __name__ == '__main__':
    unittest.main()
