import unittest
from position import Position, Polyline


# ToDo Implementieren Sie die notwendigen Tests
class TestPolyline1(unittest.TestCase):
    def testLength1(self):
        self.poly=Polyline(1)
        x1=Position(5,10)
        self.poly.add_position(x1)
        self.assertEqual(len(self.poly.positions),1)
        self.assertEqual(self.poly.length(),0)

    def testLength2(self):
        poly = Polyline(1)
        x1 = Position(0,10)
        x2 = Position(10,10)
        poly.add_position(x1)
        poly.add_position(x2)
        t = poly.length()
        self.assertEqual(t, 10)




if __name__ == '__main__':
    unittest.main()