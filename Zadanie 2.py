#ZADANIE 2
print("ZADANIE 2")

age = input("Podaj swoj wiek: ")
money = input("Ile masz pieniedzy w portfelu?: ")

if(int(age) >= 18 and int(money) >=20 ):
    print("Jestes pełnoletni i masz wystarczającą ilość pinieniędzy")
elif(int(age) >= 18 and int(money) <20):
    print("Jestes pełnoletni, ale nie masz wystarczającej ilości pieniędzy. Brakuje Ci " + str(20 - int(money)) + "zł")
elif(int(age) < 18 and int(money) > 20):
    print("Nie jestes pełnoletni, ale masz wystarczająca ilość pieniędzy. Alkohol będziesz mógł kupić za " + str(18 - int(age)) + " lat")
elif(int(age) < 18 and int(money) < 20):
    print("Nie jestes pełnoletni i nie masz wystarczającej ilości pieniędzy. Alkohol bedziesz mógł kupić za " + str(18 - int(age)) + " lat, oraz jak dozbierasz " + str(20 - int(money)) + "zł" )
