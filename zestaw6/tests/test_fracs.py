import unittest
from fracs import Frac


class TestFracs(unittest.TestCase):
    def setUp(self):
        self.f1 = Frac(1, 2)
        self.f2 = Frac(4, -5)
        self.f3 = Frac(-3, -8)
        self.f4 = Frac(-3, 6)
        self.zero = Frac(0, 1)


    def test_str(self):
        self.assertEqual(str(self.f1), "1/2")
        self.assertEqual(str(self.f2), "-4/5")
        self.assertEqual(str(self.f3), "3/8")
        self.assertEqual(str(Frac(-4, -12)), "1/3")
        self.assertEqual(str(Frac(-4, 1)), "-4")


    def test_repr(self):
        self.assertEqual(repr(self.f1), "Frac(1, 2)")
        self.assertEqual(repr(self.f2), "Frac(-4, 5)")
        self.assertEqual(repr(self.f3), "Frac(3, 8)")
        self.assertEqual(repr(Frac(-4, -12)), "Frac(1, 3)")
        self.assertEqual(repr(Frac(-4, 1)), "Frac(-4, 1)")        


    def test_cmp(self):
        self.assertEqual(self.f1.__cmp__(self.f2), 1)
        self.assertEqual(self.f4.__cmp__(self.f3), -1)
        self.assertEqual(self.f3.__cmp__(Frac(9, 24)), 0)
        self.assertEqual(Frac(3, -6).__cmp__(self.f4), 0)


    def test_eq(self):
        self.assertTrue(self.f1.__eq__(Frac(-12, -24)))
        self.assertTrue(self.f2 == Frac(-4, 5))
        self.assertTrue(self.f4 == self.f4)

        self.assertFalse(self.f2.__eq__(self.f1))
        self.assertFalse(self.f1 == self.f4)


    def test_ne(self):
        self.assertFalse(self.f1.__ne__(Frac(-12, -24)))
        self.assertFalse(self.f2 != Frac(-4, 5))
        self.assertFalse(self.f4 != self.f4)

        self.assertTrue(self.f2.__ne__(self.f1))
        self.assertTrue(self.f1 != self.f4)


    def test_lt(self):
        self.assertTrue(self.f3.__lt__(self.f1))
        self.assertTrue(self.f4 < self.f3)
        self.assertTrue(self.f2 < Frac(-30, 62))

        self.assertFalse(self.f2.__lt__(self.f2))
        self.assertFalse(self.f1 < self.f3)
        self.assertFalse(Frac(-10, -40) < self.f4)


    def test_le(self):
        self.assertTrue(self.f3.__le__(self.f1))
        self.assertTrue(self.f4 <= self.f3)
        self.assertTrue(self.f2 <= Frac(-30, 62))
        self.assertTrue(self.f2.__le__(self.f2))

        self.assertFalse(self.f4.__le__(self.f2))
        self.assertFalse(self.f1 <= self.f3)
        self.assertFalse(Frac(-10, -40) <= self.f4)


    def test_gt(self):
        self.assertFalse(self.f3.__gt__(self.f1))
        self.assertFalse(self.f4 > self.f3)
        self.assertFalse(self.f2 > Frac(-30, 62))
        self.assertFalse(self.f2.__gt__(self.f2))

        self.assertTrue(self.f3.__gt__(self.f4))
        self.assertTrue(self.f1 > self.f3)
        self.assertTrue(Frac(-10, -40) > self.f4)


    def test_ge(self):
        self.assertFalse(self.f3.__ge__(self.f1))
        self.assertFalse(self.f4 >= self.f3)
        self.assertFalse(self.f2 >= Frac(-30, 62))

        self.assertTrue(self.f2.__ge__(self.f2))
        self.assertTrue(self.f1 >= self.f3)
        self.assertTrue(Frac(-10, -40) >= self.f4)


    def test_add(self):
        self.assertEqual(self.f1.__add__(self.f4), self.zero)
        self.assertEqual(self.f4 + Frac(10, -30), Frac(-5, 6))
        self.assertEqual(self.f3 + Frac(0,8), self.f3)

        self.assertNotEqual(self.f2.__add__(self.f4), self.f3)
        self.assertNotEqual(self.f4 + self.f4, Frac(1, 4))
 

    def test_sub(self):
        self.assertEqual(self.f4.__sub__(self.f1), Frac(-1, 1))
        self.assertEqual(self.f3 - self.f4, Frac(7, 8))
        self.assertEqual(self.f2 - Frac(-4, 5), self.zero)

        self.assertNotEqual(self.f1.__sub__(self.f4), Frac(1, 4))
        self.assertNotEqual(self.f3 - self.f2, self.f1)


    def test_mul(self):
        self.assertEqual(self.f4.__mul__(self.f1), Frac(-1, 4))
        self.assertEqual(self.f3 * self.f4, Frac(-3, 16))
        self.assertEqual(self.f2 * Frac(0, -5), self.zero)

        self.assertNotEqual(self.f1.__mul__(self.f2), Frac(-2, -5))
        self.assertNotEqual(self.f3 * self.f2, self.f1)


    def test_truediv(self):
        self.assertEqual(self.f4.__truediv__(self.f1), Frac(-1, 1))
        self.assertEqual(self.f3 / self.f4, Frac(-3, 4))
        self.assertEqual(self.f2 / Frac(-4, 5), Frac(1, 1))
        self.assertEqual(Frac(0, 7) / self.f2, self.zero)

        self.assertNotEqual(self.f1.__truediv__(self.f4), Frac(1, 4))
        self.assertNotEqual(self.f3 / self.f2, self.f1)

        with self.assertRaises(ZeroDivisionError):
            _ = self.f3 / Frac(0, -5)


    def test_floordiv(self): 
        self.assertEqual(Frac(7, 3).__floordiv__(Frac(2, -3)), -4)
        self.assertEqual(self.f1 // self.f3, 1)
        self.assertEqual(self.f3 // Frac(-12, 35), -2)
        self.assertEqual(self.f4 // Frac(-3, -57), -10)
        self.assertEqual(Frac(12, 5) // Frac(5, 6), 2)


    def test_mod(self):
        self.assertEqual(Frac(7, 3) % Frac(1, 2), Frac(1, 3))
        self.assertEqual(self.f1.__mod__(self.f3), Frac(1, 8))
        self.assertEqual(self.f2 % Frac(13, 3), Frac(53, 15))
        self.assertEqual(Frac(1, 5) % Frac(-3, -2), Frac(1, 5))
        self.assertEqual(self.f1 % self.f4, self.zero)


    def test_pos(self):
        self.assertEqual(self.f1.__pos__(), self.f1)
        self.assertEqual(+self.f2, self.f2)
        self.assertEqual(+self.f3, self.f3)
        self.assertEqual(Frac(12, -17), Frac(-12, 17))


    def test_neg(self):
        self.assertEqual(self.f1.__neg__(), self.f4)
        self.assertEqual(-self.f2, Frac(4, 5))
        self.assertEqual(-Frac(-12, -48), Frac(-1, 4))
        self.assertEqual(-Frac(0, -12), self.zero)


    def test_invert(self):
        self.assertEqual(self.f1.__invert__(), Frac(2, 1))
        self.assertEqual(~self.f3, Frac(8, 3))
        self.assertEqual(~Frac(18, -9), self.f4)

        with self.assertRaises(ValueError):
            ~Frac(0, 13)


    def test_float(self):
        self.assertEqual(self.f4.__float__(), -0.5)
        self.assertEqual(self.f3.__float__(), 0.375)
        self.assertEqual(self.zero.__float__(), 0.0)
        self.assertAlmostEqual(Frac(2, -6).__float__(), -0.33, 2)
        self.assertAlmostEqual(Frac(-13, -17).__float__(), 0.76, 2)

    def tearDown(self): pass




if __name__ == '__main__':
    unittest.main()     