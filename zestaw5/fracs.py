from math import gcd   
import unittest

def check_denominator(frac):
    if frac[1]==0:
        raise ValueError('Denominator cannot be 0.')

def simplify_frac(frac):
    check_denominator(frac)
    num, den=frac       
    g=gcd(num, den)
    num//=g
    den//=g
    if den<0:
        num*=-1
        den*=-1
    return [num, den]

def add_frac(frac1, frac2):
    result_num=frac1[0]*frac2[1]+frac1[1]*frac2[0]
    result_den = frac1[1]*frac2[1]
    return simplify_frac([result_num, result_den])       

def sub_frac(frac1, frac2):      
    return add_frac(frac1, [-frac2[0], frac2[1]])  

def mul_frac(frac1, frac2): 
    result_num=frac1[0]*frac2[0]
    result_den=frac1[1]*frac2[1]
    return simplify_frac([result_num, result_den])      

def div_frac(frac1, frac2):
    if is_zero(frac2):
        raise ZeroDivisionError('Cannot divide by 0.')
    return mul_frac(frac1, [frac2[1], frac2[0]])        

def is_positive(frac):
    check_denominator(frac)
    return frac[0]*frac[1]>0         

def is_zero(frac):
    check_denominator(frac)
    return frac[0]==0                 

def cmp_frac(frac1, frac2):
    frac1=simplify_frac(frac1)
    frac2=simplify_frac(frac2)
    x=frac1[0]*frac2[1]
    y=frac2[0]*frac1[1]
    return (x>y)-(x<y)
        
def frac2float(frac):
    check_denominator(frac)
    return frac[0]/frac[1]              


#-----
class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-7,-2], [8, 4]), [11, 2])
        self.assertEqual(add_frac([0,8], [1, 8]), [1,8])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [4, 8]), self.zero)
        self.assertEqual(sub_frac([2, 4], [2,3]),[-1, 6])
        self.assertEqual(sub_frac([7, 8], [1, 5]), [27, 40])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [4, 8]), [1,4])
        self.assertEqual(mul_frac([2, 4], [2,-3]),[-1, 3])
        self.assertEqual(mul_frac([0, 8], [1, 5]), self.zero)    

    def test_div_frac(self):
        self.assertEqual(div_frac([5,6], [1,3]),[5,2] )
        self.assertEqual(div_frac([-1, 3], [2, -5]),[5, 6])
        self.assertEqual(div_frac([0,7], [-1, 2]), self.zero)
        self.assertRaises(ZeroDivisionError, div_frac, [8,7], [0,5])

    def test_is_positive(self):
        self.assertFalse(is_positive([4, -5]))
        self.assertFalse(is_positive([-4, 5]))
        self.assertFalse(is_positive([0, 5]))
        self.assertTrue(is_positive([4, 5]))
        self.assertTrue(is_positive([-4, -5]))

    def test_is_zero(self):
        self.assertFalse(is_zero([-2,7]))
        self.assertRaises(ValueError, is_zero, [8,0])
        self.assertTrue(is_zero([0,-7]))
        self.assertTrue(is_zero([-0,-7]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [-12, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [-12, -24]), 0)
        self.assertEqual(cmp_frac([1,-2], [1, 3]), -1)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, -2]), -0.50 , 2)
        self.assertAlmostEqual(frac2float([12, 36]), 0.33, 2)
        self.assertAlmostEqual(frac2float([-12, -32]), 0.375, 3)

    def tearDown(self):
        self.zero=[]



if __name__ == '__main__':
    unittest.main() 

