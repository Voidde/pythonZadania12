def fibo(x):
    if(x == 0):
        return 0
    elif(x == 1):
        return 1
    else:
        return fibo(x-1) + fibo(x - 2)

def sn(n,k):
    if k < 0 or k > n:
        return 0
    elif k == 0 or k == n:
        return 1
    else:
        return sn(n - 1, k - 1) + sn(n - 1, k)


print(str(sn(5,2)))
print(str(fibo(7)))





