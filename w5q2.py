def brute_force(password):
    length = len(password)
    attempt = 0

    for num in range(10**length):
        attempt += 1
        guess = f"{num:0{length}d}"

        if guess == password:
            print("Password cracked!")
            print("Password:", guess)
            print("Attempts:", attempt)
            return

    print("Password not found.")

passwords = ["0001", "0123", "1234", "56289123"]

for pwd in passwords:
    print("\nTrying to crack:", pwd)
    brute_force(pwd)
