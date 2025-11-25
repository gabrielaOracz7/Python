from math import gcd  

class Frac:

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError('Denominator cannot be 0')
        if isinstance(y, float):
            raise TypeError('Denominator cannot be float')
        if isinstance(x, float) and y != 1:
            raise TypeError('cannot use float when denominator != 1') 
        if isinstance(x, float):  # Frac(0.25) allowed but Frac(0.2, 0.3) or Frac(5, 0.25) or Frac(0.5, 5) not
            x, y = x.as_integer_ratio()
        g = gcd(x, y)
        x //= g
        y //= g
        if y < 0:
            x, y = -x, -y
        self.x = x
        self.y = y


    @staticmethod
    def _helper(val):
        if isinstance(val, Frac):
            return val
        elif isinstance(val, int):
            return Frac(val)
        elif isinstance(val, float):
            x, y = val.as_integer_ratio()
            return Frac(x, y)
        raise ValueError('Unsupported operand type')


    def __str__(self):
        return f'{self.x}' if self.y == 1 else f'{self.x}/{self.y}'       


    def __repr__(self):
        return f'Frac({self.x}, {self.y})'   


    def __cmp__(self, other):
        other = Frac._helper(other)
        a = self.x * other.y
        b = self.y * other.x
        return (a > b) - (a < b)
 

    def __eq__(self, other):
        other = Frac._helper(other)
        return self.x == other.x and self.y == other.y


    def __ne__(self, other):
        return not self == other


    def __lt__(self, other):
        other = Frac._helper(other)
        return self.x * other.y < self.y * other.x
   

    def __le__(self, other):
        return self < other or self == other


    def __gt__(self, other):
        return not self <= other


    def __ge__(self, other):
        return not self < other


    def __add__(self, other):
        other = Frac._helper(other)
        x = self.x * other.y + self.y * other.x
        y = self.y * other.y
        return Frac(x, y)


    __radd__ = __add__  


    def __sub__(self, other):
        other = Frac._helper(other)
        return self.__add__(-other)


    def __rsub__(self, other):
        other = self._helper(other)
        return other - self


    def __mul__(self, other):
        other = Frac._helper(other)
        return Frac(self.x * other.x, self.y * other.y)


    __rmul__ = __mul__


    def __truediv__(self, other):
        other = Frac._helper(other)
        if other.x == 0:
            raise ZeroDivisionError('Cannot divide by 0')
        return  Frac(self.x * other.y, self.y * other.x)


    def __rtruediv__(self, other):
        other = Frac._helper(other)
        return other / self


    __div__ = __truediv__
    __rdiv__ = __rtruediv__


    def __floordiv__(self, other):
        other = Frac._helper(other)
        result = self / other
        return Frac(result.x // result.y)


    def __rfloordiv__(self, other):
        other = Frac._helper(other)
        return other // self


    def __mod__(self, other):
        other = Frac._helper(other)
        q = self // other
        return self - q * other


    def __rmod__(self, other):
        other = Frac._helper(other)
        return other % self


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
   

