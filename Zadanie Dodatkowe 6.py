x = True
while x == True:
    x = False
    dzialanie = input("Podaj dzialanie jakie chcesz wykonac(Dodawanie(+),Odejmowanie(-),Mnozenie(*),Dzielenie(/):")
    if(dzialanie == '+'):
        a = input("Podaj pierwsza liczbe: ")
        b = input("Podaj druga liczbe: ")
        if a.isnumeric() and b.isnumeric():
            wynik = float(a) + float(b)
            print(f"{a} + {b} = {wynik}")
        else:
            print("Przynajmniej jedna z podanych wartosci nie jest liczba.")
    elif(dzialanie == '-'):
        a = input("Podaj pierwsza liczbe: ")
        b = input("Podaj druga liczbe: ")
        if a.isnumeric() and b.isnumeric():
            wynik = float(a) - float(b)
            print(f"{a} - {b} = {wynik}")
        else:
            print("Przynajmniej jedna z podanych wartosci nie jest liczba.")
    elif(dzialanie == '/'):
        a = input("Podaj pierwsza liczbe: ")
        b = input("Podaj druga liczbe: ")
        if b == '0':
            print("Nie mozna dzielic przez 0")
        elif a.isnumeric() and b.isnumeric() and b != 0:
            wynik = float(a) / float(b)
            print(f"{a} / {b} = {wynik}")
        else:
            print("Przynajmniej jedna z podanych wartosci nie jest liczba, lub dzielisz przez 0")

    elif(dzialanie == '*'):
        a = input("Podaj pierwsza liczbe: ")
        b = input("Podaj druga liczbe: ")
        if a.isnumeric() and b.isnumeric():
            wynik = float(a) * float(b)
            print(f"{a} * {b} = {wynik}")
        else:
            print("Przynajmniej jedna z podanych wartosci nie jest liczba.")
    else:
        print("Podaj poprawne dzialanie.")
        x = True