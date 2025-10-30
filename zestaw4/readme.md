# Zestaw 4 - funkcje

### Zadanie 4.2
Rozwiązania zadań [`3.5`](https://github.com/gabrielaOracz7/Python/blob/main/zestaw3/3_5.py) i [`3.6`](https://github.com/gabrielaOracz7/Python/blob/main/zestaw3/3_6.py) z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny `string` przez `return`. Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów. 

```python
def make_ruler(n): pass

def make_grid(rows, cols): pass
```

---

### Zadanie 4.3
Napisać iteracyjną wersję funkcji `factorial(n)` obliczającej silnię.

---

### Zadanie 4.4
Napisać iteracyjną wersję funkcji `fibonacci(n)` obliczającej n-ty wyraz ciągu Fibonacciego. 

---

### Zadanie 4.5
Napisać funkcję `odwracanie(L, left, right)` odwracającą kolejność elementów na liście od numeru `left` do `right` __włącznie__. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną. 

---

### Zadanie 4.6
Napisać funkcję `sum_seq(sequence)` obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje. 

**Wskazówka:** rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez `isinstance(item, (list, tuple))`.

---

### Zadanie 4.7
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. Napisać funkcję `flatten(sequence)`, która zwróci spłaszczoną listę wszystkich elementów sekwencji. 

**Wskazówka:** rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez `isinstance(item, (list, tuple))`. 