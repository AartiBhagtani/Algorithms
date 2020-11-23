import math
t = int(input())
    

while t:
    n = int(input())

    if n == 1:
        print(0)
    elif n == 2 or n == 3:
        print(1)
    else:
        term = int(math.log(n, 2))
        # term = math.floor(math.log2(n))
        a = term - 2
        if a%4 == 0:
            print(2)
        elif a%4 == 1:
            print(3)
        elif a%4 == 2:
            print(0)
        else:
            print(9)

            
    t -= 1