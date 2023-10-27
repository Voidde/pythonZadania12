from math import sqrt
def wzor_herona(a,b,c):
    if( float(a) + float(b) > float(c) and float(a) + float(c) > float(b) and float(b) + float(c) > float(a)):
        p = float((a + b + c)/2)
        pole = sqrt((p*(p-a)*(p-b)*(p-c)))
        return pole
    else:
        return -1

def rown_kwadr(a,b,c):
    if( a == 0 ):
        return -1
    else:
        delta = (b ** 2)- (4 * (a * c))
        print(str(delta))
        if(delta == 0 ):
            return (-b)/2*a
        elif(delta > 0 ):
            return (-b - sqrt(delta)) / (2 * a),(-b + sqrt(delta)) / (2 * a)
        else:
            return -1




print(str(wzor_herona(4,5,7)))

print(str(rown_kwadr(2,2,-12)))



