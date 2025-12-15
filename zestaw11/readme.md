# Zestaw 11 - Struktury danych

### Zadanie 11.2
Do klasy `SingleList` dodać nowe metody.

```python
class SingleList:
# ... inne metody ...

    def search(self, data): pass   # klasy O(n)
        # Zwraca łącze do węzła o podanym kluczu lub None.

    def find_min(self): pass   # klasy O(n)
        # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.

    def find_max(self): pass   # klasy O(n)
        # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.

    def reverse(self): pass   # klasy O(n)
        # Odwracanie kolejności węzłów na liście.
```