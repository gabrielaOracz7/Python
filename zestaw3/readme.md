# Zestaw 3 - instrukcje i składnia

### Zadanie 3.1
Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?
```python
# a) 
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
```
```python
# b)
for i in "axby": if ord(i) < 100: print (i)
```
```python
# c)
for i in "axby": print (ord(i) if ord(i) < 100 else i)
```

---

### Zadanie 3.2
Co jest złego w kodzie:

```python
# a)
L = [3, 5, 4] ; L = L.sort()
```
```python
# b)
x, y = 1, 2, 3
```
```python
# c)
X = 1, 2, 3 ; X[1] = 4
```
```python
# d)
X = [1, 2, 3] ; X[3] = 4
```
```python
# e)
X = "abc" ; X.append("d")
```
```python
# f)
L = list(map(pow, range(8)))
```

---

### Zadanie 3.3
Wypisać w pętli liczby od `0` do `30` z wyjątkiem liczb podzielnych przez `3`. Użyć pętli `for` lub `while`.

---

### Zadanie 3.4
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą `x` (typ `float`) i wypisujący `x` oraz jego trzecią potęgę `(x^3)`. Zatrzymanie programu następuje po wpisaniu z klawiatury `stop`. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

---

### Zadanie 3.5
Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny `string`, a potem go wypisać.

**Przykład:**
Miarka o długości 12:

```
|....|....|....|....|....|....|....|....|....|....|....|....|

0    1    2    3    4    5    6    7    8    9   10   11   12
```
---

### Zadanie 3.6
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny `string`, a potem go wypisać. 

**Przykład:**
Prostokąt składający się 2 × 4 pól ma postać:
```
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   | 
+---+---+---+---+
```
---

### Zadanie 3.8
Dla dwóch sekwencji liczb lub znaków znaleźć:

(a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń). 

---

### Zadanie 3.9
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. Znaleźć listę zawierającą sumy liczb z tych sekwencji. 

**Przykład:**
Sekwencja `[[],[4],(1,2),[3,4],(5,6,7)]` -> Spodziewany wynik `[0,4,3,7,18]`.

---

### Zadanie 3.10
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami `I, V, X, L, C, D, M`) na liczby arabskie (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja `roman2int()`]. 