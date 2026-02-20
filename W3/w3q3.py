import math

n = int(input("Enter a number: "))
count = 0

for i in range(1, n ):
    if math.gcd(i, n) == 1:
        count += 1
        print(i)

print(f"Euler Totients of {n} is {count}")
