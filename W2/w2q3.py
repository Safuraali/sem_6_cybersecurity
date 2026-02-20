def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

g = gcd(a, b)
#print("GCD is:", g)

if g == 1:
    print("The numbers are relatively prime.")
else:
    print("The numbers are not relatively prime.")
