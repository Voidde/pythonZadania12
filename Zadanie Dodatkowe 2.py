doit = True
x = 0
print("While #1")
while(doit == True):
     x += 1
     print(x)
     if(x == 1):
         doit = False

print("")
print("While #2")
while True:
    print("Cos sie tam wykonuje")
    x = input("Koniec petli?(Tak/Nie): ")
    if x == 'Tak':
        break



