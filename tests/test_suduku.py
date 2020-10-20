import unittest
from sudukusolver import SudukuSolver
from coord import Coord
import itertools

class TestSuduku(unittest.TestCase):
    def setUp(self):
        self.coords = [{'x': i, 'y': i, 'value': i} for i in range(1, 10)]
        self.suduku = SudukuSolver(self.coords)

    def tearDown(self):
        del self.suduku, self.coords

    def test_01_parse_coord_list(self):
        assert str(self.suduku.possible_values) == """                             0  ...                            8
0                            1  ...  [1, 2, 3, 4, 5, 6, 7, 8, 9]
1  [1, 2, 3, 4, 5, 6, 7, 8, 9]  ...  [1, 2, 3, 4, 5, 6, 7, 8, 9]
2  [1, 2, 3, 4, 5, 6, 7, 8, 9]  ...  [1, 2, 3, 4, 5, 6, 7, 8, 9]
3  [1, 2, 3, 4, 5, 6, 7, 8, 9]  ...  [1, 2, 3, 4, 5, 6, 7, 8, 9]
4  [1, 2, 3, 4, 5, 6, 7, 8, 9]  ...  [1, 2, 3, 4, 5, 6, 7, 8, 9]
5  [1, 2, 3, 4, 5, 6, 7, 8, 9]  ...  [1, 2, 3, 4, 5, 6, 7, 8, 9]
6  [1, 2, 3, 4, 5, 6, 7, 8, 9]  ...  [1, 2, 3, 4, 5, 6, 7, 8, 9]
7  [1, 2, 3, 4, 5, 6, 7, 8, 9]  ...  [1, 2, 3, 4, 5, 6, 7, 8, 9]
8  [1, 2, 3, 4, 5, 6, 7, 8, 9]  ...                            9

[9 rows x 9 columns]"""
        self.assertListEqual(self.suduku.unresolved_coords, [Coord(i, i) for i in range(1, 10)])

    def test_resolve_possible_values(self):
        pass

    def test_resolve_row(self):
        self.suduku.resolve_row(Coord(1,1))
        for i in list(range(1,9)):
            assert 1 not in self.suduku.possible_values.iloc[0, i]

    def test_resolve_column(self):
        self.suduku.resolve_column(Coord(1, 1))
        for i in list(range(1, 9)):
            assert 1 not in self.suduku.possible_values.iloc[i, 0]

    def test_resolve_box(self):
        self.suduku.resolve_box(Coord(1, 1))
        for (x, y) in itertools.product(list(range(1, 3)), list(range(1, 3))):
            if isinstance(self.suduku.possible_values.iloc[x, y], list):
                assert 1 not in self.suduku.possible_values.iloc[x, y]

        for (x, y) in itertools.product(list(range(4, 9)), list(range(4, 9))):
            if isinstance(self.suduku.possible_values.iloc[x, y], list):
                assert 1 in self.suduku.possible_values.iloc[x, y]




if __name__ == '__main__':
    unittest.main()
