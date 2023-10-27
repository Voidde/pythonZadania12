from datetime import datetime
#ZADANIE 1
print("ZADANIE 1")

name = input("Podaj swoje imię: ")
age = input("Podaj swój wiek: ")
year = datetime.now().year
print("Twoje imię ma " + str(len(name)) + "liter i zaczyna się od " + name[0] + ".")
print("Teraz masz " + str(age) + " lat, a za rok będzie to " + str(int(age)+1) +". Rok urodzenia to " + str(year - int(age)))
