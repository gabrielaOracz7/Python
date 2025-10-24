# ZADANIE 3.1-----------------------------------------------------------------------------

# a)
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# Powyższy  kod  nie powoduje SyntaxError (błąd  składni), jednak stosowanie średników  w 
# celu oddzielania  instrukcji czy umieszczanie  warunków   w nawiasach jest zbędne i nie 
# jest zalecane, gdyż może chociażby zaburzać czytelność kodu.

# Zalecany zapis:
x = 2
y = 3
if x>y:
    result = x
else:
    result = y


# b)
# for i in "axby": if ord(i) < 100: print (i)
# Ten fragment nie jest poprawny składniowo - Python wymaga stosowania odpowiednich  wcięć.
# Dlatego w powyższym przykładzie instrukcja warunkowa 'if' powinna znaleźć się  w kolejnej
# linii pod nagłówkiem pętli 'for' z odpowiednim wcięciem. 

# Poprawniony zapis:
for i in "axby":
    if ord(i)<100: print(i)
# lub:
for i in "axby":
    if ord(i)<100:
        print(i)


# c)
for i in "axby": print(ord(i) if ord(i) < 100 else i)
# Powyższy fragment jest składniowo poprawny. Wyrażenie '(ord(i) if ord(i)<100 else i)' to 
# przykład tzw. wyrażenia trójargumentowego.