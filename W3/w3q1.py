n = int(input("Enter a number: "))

k = 0
temp = n

while temp > 1 and temp % 2 == 0:
    temp = temp // 2
    k += 1

if temp == 1:
    print(f"{n} is in the form of 2^k (for k = {k})")
else:
    print(f"{n} is NOT in the form of 2^k")
