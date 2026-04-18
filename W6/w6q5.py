# Simplified Feistel Cipher

def xor(a, b):
    return format(int(a, 2) ^ int(b, 2), '04b')

# Simple round function (can be anything)
def round_function(right, key):
    # Example: XOR + circular shift
    temp = xor(right, key)
    return temp[1:] + temp[0]  # left shift

def feistel_encrypt(block, keys):
    left = block[:4]
    right = block[4:]

    print("\nEncryption Process:")
    for i in range(len(keys)):
        print(f"Round {i+1}:")
        temp = right
        f_output = round_function(right, keys[i])
        right = xor(left, f_output)
        left = temp

        print(f"  Left: {left}  Right: {right}")

    return left + right

def feistel_decrypt(block, keys):
    left = block[:4]
    right = block[4:]

    print("\nDecryption Process:")
    for i in range(len(keys)-1, -1, -1):
        print(f"Round {len(keys)-i}:")
        temp = left
        f_output = round_function(left, keys[i])
        left = xor(right, f_output)
        right = temp

        print(f"  Left: {left}  Right: {right}")

    return left + right

# -------- Main --------
print("Simplified Feistel Cipher")

block = input("Enter 8-bit binary plaintext: ")
rounds = int(input("Enter number of rounds: "))

keys = []
print("Enter round keys (4-bit each):")
for i in range(rounds):
    k = input(f"Key {i+1}: ")
    keys.append(k)

cipher = feistel_encrypt(block, keys)
print("\nEncrypted Block:", cipher)

plain = feistel_decrypt(cipher, keys)
print("Decrypted Block:", plain)
