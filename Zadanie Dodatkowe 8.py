for x in range(0,13,3):
    if x != 12: print(str(x), end=',')
    else: print(str(x))

x = 3
while x>=-3:
    ex = print(x, end=',') if x != -3 else print(x)
    x -= 1
