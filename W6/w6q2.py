text = input("Enter text: ")
shift = int(input("Enter shift: "))
enc = ""
for ch in text:
    if ch.isalpha():
        enc += chr((ord(ch) + shift - 97) % 26 + 97)
    else:
        enc += ch
print("Encrypted:", enc)
dec = ""
for ch in enc:
    if ch.isalpha():
        dec += chr((ord(ch) - shift - 97) % 26 + 97)
    else:
        dec += ch

print("Decrypted:", dec)
