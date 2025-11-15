from math import gcd  

class Frac:

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ZeroDivisionError('Denominator cannot be 0')
        g = gcd(x, y)
        x //= g
        y //= g
        if y < 0:
            x, y = -x, -y
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}' if self.y == 1 else f'{self.x}/{self.y}'       

    def __repr__(self):
        return f'Frac({self.x}, {self.y})'   

    def __cmp__(self, other):
        if not isinstance(other, Frac):
            return NotImplemented
        a = self.x * other.y
        b = self.y * other.x
        return (a > b) - (a < b)

    def __eq__(self, other):
        if not isinstance(other, Frac):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Frac):
            return NotImplemented
        return self.x * other.y < self.y * other.x

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __add__(self, other):
        if not isinstance(other, Frac):
            return NotImplemented
        x = self.x * other.y + self.y * other.x
        y = self.y * other.y
        return Frac(x, y)

    def __sub__(self, other):
        if not isinstance(other, Frac):
            return NotImplemented
        return self.__add__(-other)

    def __mul__(self, other):
        if not isinstance(other, Frac):
            return NotImplemented
        return Frac(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        if not isinstance(other, Frac):
            return NotImplemented
        if other.x == 0:
            raise ZeroDivisionError('Cannot divide by 0')
        return  Frac(self.x * other.y, self.y * other.x)

    def __div__(self, other):
        """ Python2 style:
        integer division if both numbers are whole (denominator = 1); otherwise - true division
        """
        if self.y == 1 and other.y == 1:
            return self.__floordiv__(other)
        return self.__truediv__(other)

    def __floordiv__(self, other):
        if not isinstance(other, Frac):
            return NotImplemented
        result = self / other
        return result.x // result.y
    
    def __mod__(self, other):
        if not isinstance(other, Frac):
            return NotImplemented
        q = self // other
        return self - Frac(q) * other

    def __pos__(self): 
        return self

    def __neg__(self):  
        return Frac(-self.x, self.y)

    def __invert__(self):
        if self.x == 0:
            raise ValueError('Cannot invert zero')  
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y

    def __hash__(self):
        return hash(float(self)) 
   
