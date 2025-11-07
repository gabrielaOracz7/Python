import unittest
import fracs


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([-7,-2], [8, 4]), [11, 2])
        self.assertEqual(fracs.add_frac([0,8], [1, 8]), [1,8])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([1, 2], [4, 8]), self.zero)
        self.assertEqual(fracs.sub_frac([2, 4], [2,3]), [-1, 6])
        self.assertEqual(fracs.sub_frac([7, 8], [1, 5]), [27, 40])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([1, 2], [4, 8]), [1,4])
        self.assertEqual(fracs.mul_frac([2, 4], [2,-3]), [-1, 3])
        self.assertEqual(fracs.mul_frac([0, 8], [1, 5]), self.zero)    

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([5,6], [1,3]), [5,2] )
        self.assertEqual(fracs.div_frac([-1, 3], [2, -5]), [5, 6])
        self.assertEqual(fracs.div_frac([0,7], [-1, 2]), self.zero)
        self.assertRaises(ZeroDivisionError, fracs.div_frac, [8,7], [0,5])

    def test_is_positive(self):
        self.assertFalse(fracs.is_positive([4, -5]))
        self.assertFalse(fracs.is_positive([-4, 5]))
        self.assertFalse(fracs.is_positive([0, 5]))
        self.assertTrue(fracs.is_positive([4, 5]))
        self.assertTrue(fracs.is_positive([-4, -5]))

    def test_is_zero(self):
        self.assertFalse(fracs.is_zero([-2,7]))
        self.assertRaises(ValueError, fracs.is_zero, [8,0])
        self.assertTrue(fracs.is_zero([0,-7]))
        self.assertTrue(fracs.is_zero([-0,-7]))

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([1, 2], [-12, 3]), 1)
        self.assertEqual(fracs.cmp_frac([1, 2], [-12, -24]), 0)
        self.assertEqual(fracs.cmp_frac([1,-2], [1, 3]), -1)

    def test_frac2float(self):
        self.assertAlmostEqual(fracs.frac2float([4, -6]), -0.67 , 2)
        self.assertAlmostEqual(fracs.frac2float([12, 36]), 0.33, 2)
        self.assertAlmostEqual(fracs.frac2float([-13, -17]), 0.76, 2)

    def tearDown(self):
        pass



if __name__ == '__main__':
   unittest.main() 
