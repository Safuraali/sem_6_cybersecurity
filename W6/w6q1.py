text = input("Enter text: ")
key = int(input("Enter XOR key: "))

encrypted = ""
for ch in text:
    encrypted += chr(ord(ch) ^ key)

print("Encrypted Text:", encrypted)

decrypted = ""
for ch in encrypted:
    decrypted += chr(ord(ch) ^ key)

print("Decrypted Text:", decrypted)


##enc = ''.join(chr(ord(c) ^ key) for c in text)
##print("Encrypted:", enc)
##
##dec = ''.join(chr(ord(c) ^ key) for c in enc)
##print("Decrypted:", dec)
