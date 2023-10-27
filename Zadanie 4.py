#ZADANIE 4
print("ZADANIE 4")

lista_art = input("Podaj liste przedmiotow: ")

produkty_lista = list(lista_art.split(','))

produkty_zbior = set(produkty_lista)

produkty_slownik = {}

for prod in produkty_zbior:
    print(prod)
    cena = input("Podaj cene produktu : ")
    produkty_slownik[prod] = int(cena)

for item in produkty_slownik:
    print(str(item) + ":" + str(produkty_slownik[item]))