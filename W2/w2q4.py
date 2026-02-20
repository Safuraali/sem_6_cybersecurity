def display_narcissistic(n):
    start = 10 ** (n - 1)
    end = 10 ** n

    for num in range(start, end):
        temp = num
        total = 0
        while temp > 0:
            digit = temp % 10
            total += digit ** n
            temp //= 10
        if total == num:
            print(num, end=", ")
n = int(input("Enter value of n: "))

display_narcissistic(n)
