import math

r = int(input("r: "))
n = int(input("n: "))

if math.gcd(r, n) != 1:
    print("Order not defined")   
else:
    k = 1
    val = r % n
    while val != 1:
        val = (val * r) % n     
        k += 1
#else:
    #k = 1
    #while pow(r, k, n) != 1:
    #    k += 1
    print(f"Order of {r} modulo({n}) is {k}")


    

    
