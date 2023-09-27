import unittest
from position import Position, Polyline


class TestPosition(unittest.TestCase):
    def test_constructor(self):
        p1 = Position(10, 20)
        self.assertEqual(p1.x, 10)
        self.assertEqual(p1.y, 20)


class TestPolyline(unittest.TestCase):
    def setUp(self):
        print('Vorher')
        self.poly = Polyline(1)

    def tearDown(self):
        print('Nachher')
        self.poly = None

    def test_positions(self):
        p1 = Position(10, 0)
        self.poly.add_position(p1)
        self.assertEqual(len(self.poly.positions), 1)
        self.assertEqual(self.poly.positions[0].x, p1.x)
        self.assertEqual(self.poly.positions[0].y, p1.y, msg=f'Die Position hätte als Y {p1.y} haben müssen')

    def test_length(self):
        p1 = Position(0, 0)
        p2 = Position(10, 0)
        self.poly.add_position(p1)
        self.poly.add_position(p2)
        result = self.poly.length()
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()