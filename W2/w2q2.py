def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

print("GCD is:", gcd(a, b))
