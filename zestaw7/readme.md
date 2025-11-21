# Zestaw 7 - Wyjątki i iteratory

### Zadanie 7.1
W pliku `fracs.py` zdefiniować klasę `Frac` wraz z potrzebnymi metodami. Wykorzystać wyjątek `ValueError` do obsługi błędów w ułamkach. 
Dodać możliwości dodawania, odejmowania, mnożenia, dzielenia,porównywania liczb `int` do ułamków (działania lewostronne i prawostronne). Dodatkowo, rozważyć możliwość włączenia liczb `float` do działań na ułamkach

***Wskazówka:*** metoda `float.as_integer_ratio()`. 

```python
class Frac:
    """Klasa reprezentująca ułamki"""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        self.x = x
        self.y = y

    def __str__(self): pass            # zwraca "x/y" lub "x" dla y=1

    def __repr__(self): pass           # zwraca "Frac(x, y)"

    def __cmp__(self, other): pass     # cmp(frac1, frac2), Py2

    def __eq__(self, other): pass

    def __ne__(self, other): pass

    def __lt__(self, other): pass

    def __le__(self, other): pass

    def __gt__(self, other): pass

    def __ge__(self, other): pass

    def __add__(self, other): pass          # frac1+frac2, frac+int

    __radd__ = __add__                      # int+frac

    def __sub__(self, other): pass          # frac1-frac2, frac-int

    def __rsub__(self, other):              # int-frac
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other): pass          # frac1*frac2, frac*int

    __rmul__ = __mul__                      # int*frac

    def __div__(self, other): pass          # frac1/frac2, frac/int, Py2

    def __rdiv__(self, other): pass         # int/frac, Py2

    def __truediv__(self, other): pass      # frac1/frac2, frac/int, Py3

    def __rtruediv__(self, other): pass     # int/frac, Py3

    def __pos__(self):              # +frac = (+1)*frac
        return self

    def __neg__(self): pass         # -frac = (-1)*frac

    def __invert__(self): pass      # odwrotnosc: ~frac

    def __float__(self): pass       # float(frac)

    def __hash__(self):
        return hash(float(self)) 
```
---

### Zadanie 7.6
Stworzyć następujące iteratory nieskończone:

(a) zwracający `0`, `1`, `0`, `1`, `0`, `1`, ...,

(b) zwracający przypadkowo jedną wartość z (`"N"`, `"E"`, `"S"`, `"W"`) [błądzenie przypadkowe na sieci kwadratowej 2D],

(c) zwracający `0`, `1`, `2`, `3`, `4`, `5`, `6`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, ... [numery dni tygodnia]. 