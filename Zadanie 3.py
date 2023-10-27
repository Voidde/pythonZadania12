#ZADANIE 3
print("ZADANIE 3")

z = False

while(z != True):
    x = input("Chcesz wpisac dochod roczny czy miesieczny?: ")
    if(x == 'roczny' or x == 'miesieczny' ):
        z = True

money = float(input("Podaj swoj dochod: "))

if(x == 'miesieczny'):
    money *= 12

if(money <= 120000):
    print("Podatek wynosi: " + str(0.12 * money) + "zł")
elif(money >120000):
    y = money - 120000
    pdt = 0.32 * y + 0.12 * 120000
    print("Podatek wynosi: " + "%.2f " %pdt + "zł")




