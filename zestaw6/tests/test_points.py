import unittest
from points import Point

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.a = Point(1, 2)
        self.b = Point(-4, 5)
        self.c = Point(3, 3)
        self.d = Point(3, 3)


    def test_str(self):
        self.assertEqual(self.a.__str__(), "(1, 2)")
        self.assertEqual(str(self.c), "(3, 3)")
        self.assertEqual(str(self.b), "(-4, 5)")


    def test_repr(self):
        self.assertEqual(self.a.__repr__(), "Point(1, 2)")
        self.assertEqual(repr(self.b), "Point(-4, 5)")
        self.assertEqual(repr(self.c), "Point(3, 3)")


    def test_eq(self):
        self.assertFalse(self.a.__eq__(self.b))
        self.assertFalse(self.d == self.a)
        self.assertFalse(self.b == self.c)

        self.assertTrue(self.c == self.d)
        self.assertTrue(self.a.__eq__(Point(1, 2)))


    def test_ne(self):
        self.assertFalse(self.c.__ne__(self.d))
        self.assertFalse(self.b.__ne__(self.b))
        self.assertFalse(self.a != Point(1, 2))

        self.assertTrue(self.a.__ne__(self.d))
        self.assertTrue(self.a != self.b)
        self.assertTrue(self.b != Point(-4, -5))


    def test_add(self):
        self.assertEqual(self.a.__add__(self.c), Point(4, 5))
        self.assertEqual(self.b.__add__(self.d), Point(-1, 8))
        self.assertEqual(self.d + Point(10, 10), Point(13, 13))
        self.assertEqual(Point(10.25, 1.25) + Point(-5.75, 15.5), Point(4.5, 16.75))

        self.assertNotEqual(self.d + self.b, Point(1, -8))
        self.assertNotEqual(self.b.__add__(Point(23, 24)), Point(1, 1))


    def test_sub(self):
        self.assertEqual(self.a.__sub__(self.c), Point(-2, -1))
        self.assertEqual(self.b.__sub__(self.d), Point(-7, 2))
        self.assertEqual(self.d - Point(10, 10), Point(-7, -7))
        self.assertEqual(Point(10.25, 1.25) - Point(-5.75, 15.5), Point(16.0, -14.25))

        self.assertNotEqual(self.d - self.b, Point(-2, -2.5))
        self.assertNotEqual(self.b.__sub__(Point(23, 24)), Point(19, -19))
        

    def test_mul(self):
        self.assertEqual(self.a.__mul__(self.c), 9)
        self.assertEqual(self.b * self.a, 6)
        self.assertEqual(self.d.__mul__(Point(10, 2.2)), 36.6)
        self.assertEqual(Point(1.5, 2) * Point(0, -18), -36)

        self.assertNotEqual(self.a.__mul__(self.d), -9)
        self.assertNotEqual(Point(-1, 2) * Point(-1, -2), 3)


    def test_cross(self):
        self.assertEqual(self.a.cross(self.c), -3)
        self.assertEqual(self.c.cross(self.b), 27)
        self.assertEqual(self.b.cross(Point(-1.5, -3.75)), 22.5)
        self.assertAlmostEqual(Point(-1.234, 1.234).cross(Point(9.876, 9.876)), -24.374, 3)

        with self.assertRaises(TypeError):
            _ = self.b.cross((1, 2))

    def test_length(self):
        self.assertAlmostEqual(self.a.length(), 2.236, 3)
        self.assertAlmostEqual(self.c.length(), 4.24, 2)
        self.assertAlmostEqual(self.b.length(), 6.403, 3)
        self.assertEqual(Point(-6, 8).length(), 10)


    def tearDown(self): pass




if __name__ == '__main__':
    unittest.main()     