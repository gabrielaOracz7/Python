# Zestaw 6 - Klasy

### Zadanie 6.2
W pliku `points.py` zdefiniować klasę `Point` wraz z potrzebnymi metodami. Punkty są traktowane jak wektory zaczepione w początku układu współrzędnych, o końcu w położeniu `(x, y)`. Napisać kod testujący moduł `points`.

```python
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self): pass         # zwraca string "(x, y)"

    def __repr__(self): pass        # zwraca string "Point(x, y)"

    def __eq__(self, other): pass   # obsługa point1 == point2

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other


    # Punkty jako wektory 2D.
    def __add__(self, other): pass  # v1 + v2

    def __sub__(self, other): pass  # v1 - v2

    def __mul__(self, other): pass  # v1 * v2, iloczyn skalarny, zwraca liczbę

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self): pass          # długość wektora

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

```

---


### Zadanie 6.5
W pliku `fracs.py` zdefiniować klasę `Frac` wraz z potrzebnymi metodami. Ułamek jest reprezentowany przez parę liczb całkowitych. Napisać kod testujący moduł `fracs`.

```python
from math import gcd   

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self): pass         # zwraca "x/y" lub "x" dla y=1

    def __repr__(self): pass        # zwraca "Frac(x, y)"

    def __cmp__(self, other): pass  # cmp(frac1, frac2)    # Py2

    def __eq__(self, other): pass    # Py2.7 i Py3

    def __ne__(self, other): pass

    def __lt__(self, other): pass

    def __le__(self, other): pass

    def __gt__(self, other): pass

    def __ge__(self, other): pass

    def __add__(self, other): pass   # frac1 + frac2

    def __sub__(self, other): pass  # frac1 - frac2

    def __mul__(self, other): pass  # frac1 * frac2

    def __div__(self, other): pass  # frac1 / frac2, Py2

    def __truediv__(self, other): pass  # frac1 / frac2, Py3

    def __floordiv__(self, other): pass  # frac1 // frac2, opcjonalnie

    def __mod__(self, other): pass  # frac1 % frac2, opcjonalnie


    # operatory jednoargumentowe
    def __pos__(self):              # +frac = (+1)*frac
        return self

    def __neg__(self):              # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):           # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self): pass       # float(frac)

    def __hash__(self):
        return hash(float(self))   
    

```