# Zestaw 5 - Moduły

### Zadanie 5.2
Stworzyć plik `fracs.py` i zapisać w nim funkcje do działań na ułamkach. Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych: `[licznik, mianownik]`. Napisać kod testujący moduł fracs. **Nie należy korzystać z klasy `Fraction` z modułu `fractions`.** Można wykorzystać funkcję  `math.gcd()` implementującą algorytm Euklidesa. 


Moduł `fracs.py` powinien udostępniać następujące operacje na ułamkach:
```python
def add_frac(frac1, frac2): pass        # frac1 + frac2

def sub_frac(frac1, frac2): pass        # frac1 - frac2

def mul_frac(frac1, frac2): pass        # frac1 * frac2

def div_frac(frac1, frac2): pass        # frac1 / frac2

def is_positive(frac): pass             # bool, czy dodatni

def is_zero(frac): pass                 # bool, typu [0, x]

def cmp_frac(frac1, frac2): pass        # -1 | 0 | +1

def frac2float(frac): pass              # konwersja do float
```