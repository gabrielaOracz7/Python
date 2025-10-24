# ZADANIE 3.4----------------------------------------------------------------------

while True:
    x=input("Type a number (or 'stop' to quit):  ")
    if x.lower()=='stop':
        break
    try:
        x=float(x)
        print('Your number x: ', x, "and its cube (x^3): ", x**3, "\n")
    except ValueError:
        print("Wrong input. It must be a number or 'stop' if you want to quit.")
