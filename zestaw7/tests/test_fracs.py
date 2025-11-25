import unittest
from fracs import Frac


class TestFracs(unittest.TestCase):
    def setUp(self):
        self.frac1 = Frac(1, 2)
        self.frac2 = Frac(-3, -8)
        self.frac3 = Frac(-3, 6)
        self.zero = Frac(0, 1)

        self.int1 = 12
        self.int2 = -10

        self.float1 = 10.5
        self.float2 = -2.75


    def test_str(self):
        self.assertEqual(str(self.frac1), "1/2")
        self.assertEqual(str(self.frac2), "3/8")
        self.assertEqual(str(Frac(-4, 12)), "-1/3")
        self.assertEqual(str(Frac(-4, 1)), "-4")
        self.assertEqual(str(Frac(self.int1)), "12")
        self.assertEqual(str(Frac(self.int2)), "-10")
        self.assertEqual(str(Frac(self.float1)), "21/2")
        self.assertEqual(str(Frac(self.float2)), "-11/4")
        
        with self.assertRaises(ValueError):
            str(Frac(-12, 0))

        with self.assertRaises(TypeError):
            str(Frac(0.25, 0.3))

        with self.assertRaises(TypeError):
            str(Frac(5, 0.6))

    
    def test_repr(self):
        self.assertEqual(repr(self.frac1), "Frac(1, 2)")
        self.assertEqual(repr(self.frac2), "Frac(3, 8)")
        self.assertEqual(repr(Frac(-4, 12)), "Frac(-1, 3)")
        self.assertEqual(repr(Frac(self.int1)), "Frac(12, 1)")        
        self.assertEqual(repr(Frac(self.int2)), "Frac(-10, 1)")        
        self.assertEqual(repr(Frac(self.float1)), "Frac(21, 2)")        
        self.assertEqual(repr(Frac(self.float2)), "Frac(-11, 4)")        


    def test_cmp(self):
        self.assertEqual(self.frac1.__cmp__(self.frac2), 1)
        self.assertEqual(self.frac3.__cmp__(self.frac2), -1)
        self.assertEqual(self.frac1.__cmp__(Frac(9, 18)), 0)
        self.assertEqual(Frac(3, -6).__cmp__(5), -1)
        self.assertEqual(Frac(3, -6).__cmp__(-0.5), 0)
        self.assertEqual(Frac(-3, -6).__cmp__(self.int2), 1)

        with self.assertRaises(ValueError):
            Frac(10).__cmp__([1, 2, 3])


    def test_eq(self):
        self.assertTrue(self.frac1.__eq__(Frac(-12, -24)))
        self.assertTrue(self.frac3 == self.frac3)
        self.assertTrue(Frac(10,2) == 5)
        self.assertTrue(Frac(-42, -4) == self.float1)
        self.assertTrue(-10 == Frac(40, -4))
        self.assertTrue(-12.75 == Frac(51, -4))

        self.assertFalse(self.frac2.__eq__(self.frac1))
        self.assertFalse(self.frac1 == self.frac3)
        self.assertFalse(Frac(12, 2) == -6)
        self.assertFalse(Frac(-13, 5) == 2.6)
        self.assertFalse(self.int1 == Frac(15))
        self.assertFalse(self.float1 == Frac(10,3))

        with self.assertRaises(ValueError):
            'str' == Frac(10)

        with self.assertRaises(ValueError):
            Frac(10) == [1, 2, 3]


    def test_lt(self):
        self.assertTrue(self.frac2.__lt__(self.frac1))
        self.assertTrue(self.frac3 < self.frac2)
        self.assertTrue(Frac(-4, 5) < Frac(-30, 62))
        self.assertTrue(self.int2 < self.frac2)
        self.assertTrue(self.float2 < self.frac1)
        self.assertTrue(Frac(3, 7) < 5)
        self.assertTrue(Frac(-12, 5) < self.float1)

        self.assertFalse(self.frac2.__lt__(self.frac2))
        self.assertFalse(self.frac1 < self.frac2)
        self.assertFalse(Frac(-10, -40) < self.frac3)
        self.assertFalse(self.int1 < self.frac1)
        self.assertFalse(self.float1 < self.frac1)
        self.assertFalse(self.frac1 < -10)
        self.assertFalse(self.frac2 < -0.75)

        with self.assertRaises(ValueError):
            'str' < Frac(10)

        with self.assertRaises(ValueError):
            Frac(10) < [1, 2, 3]


    def test_le(self):
        self.assertTrue(self.frac2.__le__(self.frac1))
        self.assertTrue(self.frac3 <= self.frac2)
        self.assertTrue(self.frac3 <= Frac(-30, 62))
        self.assertTrue(self.frac2 <= (self.frac2))
        self.assertTrue(self.int1 <= Frac(24, 2))
        self.assertTrue(self.float2 <= self.frac1)
        self.assertTrue(self.frac3 <= 8)
        self.assertTrue(self.frac2 <= 1.7557)

        self.assertFalse(self.frac1.__le__(self.frac3))
        self.assertFalse(self.frac1 <= self.frac2)
        self.assertFalse(Frac(-10, -40) <= self.frac3)
        self.assertFalse(self.int1 <= Frac(13, 5))
        self.assertFalse(0.75 <= Frac(-4, 3))
        self.assertFalse(Frac(12, 5) <= self.int2)
        self.assertFalse(self.frac1 <= -0.7555)

        with self.assertRaises(ValueError):
            'str' <= Frac(10)

        with self.assertRaises(ValueError):
            Frac(10) <= [1, 2, 3]


    def test_gt(self):
        self.assertTrue(self.frac2.__gt__(self.frac3))
        self.assertTrue(self.frac1 > self.frac2)
        self.assertTrue(Frac(-10, -40) > self.frac3)
        self.assertTrue(5 > Frac(1, 2))
        self.assertTrue(0.7556 > self.frac3)
        self.assertTrue(self.frac1 > -15)
        self.assertTrue(Frac(13, 6) > -0.25)

        self.assertFalse(self.frac2.__gt__(self.frac1))
        self.assertFalse(self.frac3 > self.frac2)
        self.assertFalse(self.frac3 > Frac(30, 62))
        self.assertFalse(self.frac3 > (self.frac3))
        self.assertFalse(-10 > self.frac1)
        self.assertFalse(-0.75 > self.zero)
        self.assertFalse(Frac(12, 6) > 2)
        self.assertFalse(self.frac3 > self.float1)

        with self.assertRaises(ValueError):
            'str' > Frac(10)

        with self.assertRaises(ValueError):
            Frac(10) > [1, 2, 3]


    def test_ge(self):
        self.assertTrue(self.frac2.__ge__(self.frac2))
        self.assertTrue(self.frac1 >= self.frac2)
        self.assertTrue(Frac(-10, -40) >= self.frac3)
        self.assertTrue(5 >= self.frac3)
        self.assertTrue(0.75 >= Frac(3, 4))
        self.assertTrue(self.frac2 >= self.int2)
        self.assertTrue(Frac(12, 5) >= self.float2)

        self.assertFalse(self.frac2.__ge__(self.frac1))
        self.assertFalse(self.frac3 >= self.frac2)
        self.assertFalse(self.frac3 >= Frac(-30, 62))
        self.assertFalse(-12 >= Frac(24, 2))
        self.assertFalse(self.float2 >= self.frac1)
        self.assertFalse(Frac(12, 3) >= 123)
        self.assertFalse(Frac(-24, 7) >= 12.345)

        with self.assertRaises(ValueError):
            'str' >= Frac(10)

        with self.assertRaises(ValueError):
            Frac(10) >= [1, 2, 3]


    def test_add(self):
        self.assertEqual(self.frac1.__add__(self.frac3), self.zero)
        self.assertEqual(self.frac3 + Frac(10, -30), Frac(-5, 6))
        self.assertEqual(self.frac2 + Frac(0,8), self.frac2)
        self.assertEqual(5 + Frac(12, 5), Frac(37, 5))
        self.assertEqual(self.float2 + self.frac1, Frac(-9, 4))
        self.assertEqual(self.frac2 + 10, Frac(83, 8))
        self.assertEqual(self.frac1 + self.float1, Frac(11))

        self.assertNotEqual(self.frac3.__add__(self.frac3), Frac(-1, 4))
        self.assertNotEqual(self.frac3 + self.frac3, Frac(1, 4))
        self.assertNotEqual(5 + Frac(2, 4), Frac(9, 2))
        self.assertNotEqual(self.float1 + self.frac3, Frac(11))
        self.assertNotEqual(Frac(-5, 3) + 5, Frac(-10, 3))
        self.assertNotEqual(self.frac1 + 0.85, Frac(-12, 5))

        with self.assertRaises(ValueError):
            _ = 'str' + Frac(10)

        with self.assertRaises(ValueError):
            _ = Frac(10) + [1, 2, 3]


    def test_sub(self):
        self.assertEqual(self.frac3.__sub__(self.frac1), Frac(-1, 1))
        self.assertEqual(self.frac2 - self.frac3, Frac(7, 8))
        self.assertEqual(self.frac1 - Frac(-4, -8), self.zero)
        self.assertEqual(self.int1 - self.frac1, Frac(23, 2))
        self.assertEqual(0.75 - self.frac3, Frac(5, 4))
        self.assertEqual(Frac(-13, 6) - (-2), Frac(1, -6))
        self.assertEqual(self.frac2 - self.float2, Frac(25, 8))

        self.assertNotEqual(self.frac1.__sub__(self.frac3), Frac(1, 4))
        self.assertNotEqual(self.frac2 - Frac(1, 8), self.frac1)
        self.assertNotEqual(15 - self.frac1, Frac(31, 2))
        self.assertNotEqual(-0.75 - self.frac2, Frac(16, 7))
        self.assertNotEqual(Frac(13, 5) - 2, Frac(-3, 5))
        self.assertNotEqual(self.zero - self.float1, Frac(21, 2))

        with self.assertRaises(ValueError):
            _ = 'str' - Frac(10)

        with self.assertRaises(ValueError):
            _ = Frac(10) - [1, 2, 3]


    def test_mul(self):
        self.assertEqual(self.frac3.__mul__(self.frac1), Frac(-1, 4))
        self.assertEqual(self.frac2 * self.frac3, Frac(-3, 16))
        self.assertEqual(self.frac3 * Frac(0, -5), self.zero)
        self.assertEqual(self.int1 * Frac(3, 4), Frac(9))
        self.assertEqual(0.75 * self.frac3, Frac(-3, 8))
        self.assertEqual(Frac(2, 3) * 10, Frac(20, 3))
        self.assertEqual(self.frac2 * self.float2, Frac(-33, 32))
        self.assertEqual(0.1234567 * self.zero, self.zero)

        self.assertNotEqual(self.frac1.__mul__(self.frac1), Frac(-2, -5))
        self.assertNotEqual(self.frac2 * self.frac3, self.frac1)
        self.assertNotEqual(15 * self.frac1, Frac(-15, 2))
        self.assertNotEqual(self.float1 * Frac(1, 2), self.frac2)
        self.assertNotEqual(Frac(15, 2) * self.int2, Frac(75))
        self.assertNotEqual(self.frac3 * 0.45, Frac(-9, -40))

        with self.assertRaises(ValueError):
            _ = 'str' * Frac(10)

        with self.assertRaises(ValueError):
            _ = Frac(10) * [1, 2, 3]


    def test_truediv(self):
        self.assertEqual(self.frac3.__truediv__(self.frac1), Frac(-1, 1))
        self.assertEqual(self.frac2 / self.frac3, Frac(-3, 4))
        self.assertEqual(self.frac1 / Frac(-4, -8), Frac(1, 1))
        self.assertEqual(Frac(0, 7) / self.frac3, self.zero)
        self.assertEqual(self.int1 / self.frac1, Frac(24))
        self.assertEqual(1.75 / self.frac2 ,Frac(14,3))
        self.assertEqual(self.frac3 / 10, Frac(1, -20))
        self.assertEqual(Frac(15, 8) / self.float2, Frac(15, -22))

        self.assertNotEqual(self.frac1.__truediv__(self.frac3), Frac(1, 4))
        self.assertNotEqual(self.frac2 / self.frac3, self.frac1)
        self.assertNotEqual(self.int2 / self.frac3, Frac(-20))
        self.assertNotEqual(self.float1 / Frac(5, 7), Frac(-147, 10))
        self.assertNotEqual(self.frac1 / 2, Frac(-1, 4))
        self.assertNotEqual(self.frac2 / 0.75, self.frac3)

        with self.assertRaises(ZeroDivisionError):
            _ = 15 / Frac(0, -5)

        with self.assertRaises(ZeroDivisionError):
            _ = self.frac3 / Frac(0, 14)

        with self.assertRaises(ValueError):
            _ = 'str' / Frac(10)

        with self.assertRaises(ValueError):
            _ = Frac(10) / [1, 2, 3]


    def test_floordiv(self): 
        self.assertEqual(Frac(7, 3).__floordiv__(Frac(2, -3)), Frac(-4))
        self.assertEqual(self.frac1 // self.frac2, Frac(1))
        self.assertEqual(self.frac2 // Frac(-12, 35), Frac(-2))
        self.assertEqual(self.frac3 // Frac(-3, -57), Frac(-10))
        self.assertEqual(Frac(12, 5) // Frac(5, 6), Frac(2))
        self.assertEqual(13 // self.frac2, Frac(34))    
        self.assertEqual(self.float2 // Frac(-3, -13), Frac(-12))    
        self.assertEqual(self.frac3 // self.int2, self.zero)    
        self.assertEqual(Frac(15, 13) // 0.75, Frac(1))    

        with self.assertRaises(ZeroDivisionError):
            _ = 12 // Frac(0, 12)

        with self.assertRaises(ZeroDivisionError):
            _ = Frac(1, 2) // Frac(0, -13)

        with self.assertRaises(ValueError):
            _ = 'str' // Frac(10)

        with self.assertRaises(ValueError):
            _ = Frac(10) // [1, 2, 3]


    def test_mod(self):
        self.assertEqual(Frac(7, 3) % Frac(1, 2), Frac(1, 3))
        self.assertEqual(self.frac1.__mod__(self.frac2), Frac(1, 8))
        self.assertEqual(Frac(-4, 5) % Frac(13, 3), Frac(53, 15))
        self.assertEqual(Frac(1, 5) % Frac(-3, -2), Frac(1, 5))
        self.assertEqual(self.frac1 % self.frac3, self.zero)
        self.assertEqual(self.int1 % Frac(5, 7), Frac(4, 7))
        self.assertEqual(self.float1 % Frac(3, 9), Frac(1, 6) )
        self.assertEqual(Frac(83, 3) % 5, Frac(8, 3))
        self.assertEqual(Frac(-1, 5) % 0.125, Frac(1, 20))

        with self.assertRaises(ValueError):
            _ = {'a' : 1} % Frac(10)

        with self.assertRaises(ValueError):
            _ = Frac(10) % [1, 2, 3]


    def test_pos(self):
        self.assertEqual(self.frac1.__pos__(), self.frac1)
        self.assertEqual(+self.frac3, self.frac3)
        self.assertEqual(+self.frac2, self.frac2)
        self.assertEqual(+Frac(12, -17), Frac(-12, 17))
        self.assertEqual(+Frac(0.25), Frac(1, 4))
        self.assertEqual(+Frac(-1999990), Frac(-1999990))
        self.assertEqual(+Frac(-0.375), Frac(-3, 8))


    def test_neg(self):
        self.assertEqual(self.frac1.__neg__(), self.frac3)
        self.assertEqual(-self.frac2, Frac(-3, 8))
        self.assertEqual(-Frac(-12, -48), Frac(-1, 4))
        self.assertEqual(-Frac(0, -12), self.zero)
        self.assertEqual(-Frac(-6), Frac(6))
        self.assertEqual(-Frac(123), Frac(-123))
        self.assertEqual(-self.float2, Frac(11, 4))
        self.assertEqual(-Frac(10.75), Frac(43, -4))


    def test_invert(self):
        self.assertEqual(self.frac1.__invert__(), Frac(2, 1))
        self.assertEqual(~self.frac2, Frac(8, 3))
        self.assertEqual(~Frac(18, -9), self.frac3)
        self.assertEqual(~Frac(5), Frac(1, 5))
        self.assertEqual(~Frac(-2), self.frac3)
        self.assertEqual(~Frac(-2.75), Frac(-4, 11))

        with self.assertRaises(ValueError):
            ~Frac(0, 13)


    def test_float(self):
        self.assertEqual(self.frac3.__float__(), -0.5)
        self.assertEqual(self.frac2.__float__(), 0.375)
        self.assertEqual(float(self.zero), 0.0)
        self.assertEqual(float(Frac(5)), 5)
        self.assertEqual(Frac(-0.789).__float__(), -0.789)
        self.assertAlmostEqual(float(Frac(2, -6)), -0.33, 2)
        self.assertAlmostEqual(float(Frac(-13, -17)), 0.76, 2)


    def tearDown(self): pass




if __name__ == '__main__':
    unittest.main()     


    