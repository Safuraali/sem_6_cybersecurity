# Diffie-Hellman Key Exchange

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_primitive_root(g, p):
    required_set = set(range(1, p))
    actual_set = set(pow(g, k, p) for k in range(1, p))
    return required_set == actual_set

while True:
    p = int(input("Enter a prime number (p): "))
    if is_prime(p):
        break
    else:
        print("Not a prime number. Please enter a prime.")

while True:
    g = int(input("Enter a primitive root (g): "))
    if 1 < g < p and is_primitive_root(g, p):
        break
    else:
        print(f"{g} is not a primitive root modulo {p}. Try again.")

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

#Public keys
A = pow(g, a, p)
B = pow(g, b, p)

#Shared secret
secret_alice = pow(B, a, p)
secret_bob = pow(A, b, p)

print(f"Alice's public key: {A}")
print(f"Bob's public key: {B}")
print(f"Shared secret (Alice): {secret_alice}")
print(f"Shared secret (Bob): {secret_bob}")
