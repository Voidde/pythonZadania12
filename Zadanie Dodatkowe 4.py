def fun_ite(x):
    for i in range(1,x + 1):
        print("*" * i)

def fun_rek(x, y = 1):
    if y > x:
        return
    print('*' * y)
    fun_rek(x, y + 1)

fun_ite(5)
fun_rek(5)