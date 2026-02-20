n = int(input("Enter a prime number: "))

k = 1

while (2**k - 1) <= n:
    if 2**k - 1 == n:
        print(f"{n} is a Mersenne prime")
        break
    k += 1
else:
    print("Not Mersenne prime")

