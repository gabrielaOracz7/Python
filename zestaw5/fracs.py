from math import gcd   

def check_denominator(frac):
    if frac[1] == 0:
        raise ValueError('Denominator cannot be 0.')

def simplify_frac(frac):
    check_denominator(frac)
    num, den = frac       
    g = gcd(num, den)
    num //= g
    den //= g
    if den < 0:
        num *= -1
        den *= -1
    return [num, den]

def add_frac(frac1, frac2):
    result_num = frac1[0] * frac2[1] + frac1[1] * frac2[0]
    result_den = frac1[1] * frac2[1]
    return simplify_frac([result_num, result_den])       

def sub_frac(frac1, frac2):      
    return add_frac(frac1, [-frac2[0], frac2[1]])  

def mul_frac(frac1, frac2): 
    result_num = frac1[0] * frac2[0]
    result_den = frac1[1] * frac2[1]
    return simplify_frac([result_num, result_den])      

def div_frac(frac1, frac2):
    if is_zero(frac2):
        raise ZeroDivisionError('Cannot divide by 0.')
    return mul_frac(frac1, [frac2[1], frac2[0]])        

def is_positive(frac):
    check_denominator(frac)
    return frac[0] * frac[1] > 0         

def is_zero(frac):
    check_denominator(frac)
    return frac[0] == 0                 

def cmp_frac(frac1, frac2):
    frac1 = simplify_frac(frac1)
    frac2 = simplify_frac(frac2)
    x = frac1[0] * frac2[1]
    y = frac2[0] * frac1[1]
    return (x > y) - (x < y)
        
def frac2float(frac):
    check_denominator(frac)
    return frac[0] / frac[1]              



