# ZADANIE 3.2-------------------------------------------------------------

# a)
L = [3, 5, 4] ; L = L.sort()
# Funkcja sort() sortuje listę w miejscu  - modyfikuje  istniejącą  listę,
# na której  została  wywołana   i  zwraca  None. Dlatego  L po  wykonaniu 
# L = L.sort() zamiast listy przyjmuje 'wartość' None. 
 
# Poprawiona wersja, która działa zgodnie z oczekiwaniami:
L = [3,5,4] ; L.sort()


# b)
# x, y = 1, 2, 3
# Powyższa linijka kodu jest niepoprawna, ponieważ próbujemy w niej przypi-
# sać trzy literały do  dwóch zmiennych.  Aby  kod  wykonywał się poprawnie 
# liczba literałów musi być równa liczbie zmiennych.

# Poprawiona wersja:
x,y,z = 1,2,3


# c)
# X = 1, 2, 3 ; X[1] = 4
# Powyższa linijka kodu jest niepoprawna, ponieważ krotki w Pythonie są nie-
# modyfikowalne - nie można zmieniać elementów krotki po jej utworzeniu.


# d)
# X = [1, 2, 3] ; X[3] = 4
# Listy  pozwalają  na zmienianie  wartości  ich istniejących elementów (np. 
# X[2] = 4 byłoby poprawne), ale  nie  można  przypisać wartości do indeksu, 
# który wykracza poza aktualny rozmiar listy (tutaj: poza indeksy 0-2). 

# Poprawiona wersja - jeżeli intencją X[3] = 4 było umieszczenie  wartości 4 
# na  trzecim  indeksie listy X, to w  tym przypadku problem ten  rozwiązuje 
# funkcja append(), która dodaje element na  koniec listy (w  tym  przypadku 
# będzie to umieszczenie na indeksie nr 3):
X=[1,2,3] ; X.append(4)


# e)
# X = "abc" ; X.append("d")
# Funkcja append() przeznaczona jest dla list, nie stringów. 

# Poprawiona wersja:
X="abc" ; X+="d" 


# f)
# L = list(map(pow, range(8)))
# Powyżej problemem jest brak drugiego argumentu dla  funkcji pow() - Python 
# nie wie, do której potęgi chcemy podnosić liczby.