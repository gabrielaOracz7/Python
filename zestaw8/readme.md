# Zestaw 8 - Dekoratory i metaklasy

### Zadanie 8.2
Wzbogacić klasę `Triangle` o nowe funkcjonalności (plik `triangles.py`).

Stworzyć metodę klasy o nazwie `from_points`, która pozwoli utworzyć trójkąt z listy lub krotki zawierającej trzy punkty. Wywołanie:
```python
triangle = Triangle.from_points((point1, point2, point3))
```

---

Za pomocą dekoratora `@property` dodać atrybuty wirtualne zwracające liczbę (współrzędną tylko do odczytu): `top`, `left`, `bottom`, `right`, `width`, `height`. Dodać atrybuty wirtualne zwracające `Point` (tylko do odczytu): `topleft`, `bottomleft`, `topright`, `bottomright`. Wymienione atrybuty wirtualne opisują prostokąt ograniczający dany trójkąt (_bounding box_). Można rozważyć zamianę metody `center()` na atrybut wirtualny.

W osobnym pliku (`test_triangles.py`) przygotować testy klasy `Triangle` w formacie dla modułu `pytest`. 