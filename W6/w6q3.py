key = input("Enter key: ").upper().replace("J","I")
text = input("Enter text: ").upper().replace("J","I").replace(" ","")

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
matrix = ""
for c in key + alphabet:
    if c not in matrix:
        matrix += c

print("\nKey Matrix:")
for i in range(0,25,5):
    print(matrix[i:i+5])

pairs = []
i = 0
while i < len(text):
    a = text[i]
    b = text[i+1] if i+1 < len(text) else 'X'
    if a == b:
        pairs.append(a+'X')
        i += 1
    else:
        pairs.append(a+b)
        i += 2

print("Pairs:", pairs)

def playfair(pairs, mode='encrypt'):
    cipher = ""
    for p in pairs:
        a, b = p[0], p[1]

        index1 = matrix.index(a)
        r1 = index1 // 5
        c1 = index1 % 5

        index2 = matrix.index(b)
        r2 = index2 // 5
        c2 = index2 % 5

        if r1 == r2: 
            shift = 1 if mode=='encrypt' else -1
            cipher += matrix[r1*5 + (c1+shift)%5]
            cipher += matrix[r2*5 + (c2+shift)%5]
        elif c1 == c2:  
            shift = 1 if mode=='encrypt' else -1
            cipher += matrix[((r1+shift)%5)*5 + c1]
            cipher += matrix[((r2+shift)%5)*5 + c2]
        else: 
            cipher += matrix[r1*5 + c2]
            cipher += matrix[r2*5 + c1]

    return cipher

encrypted = playfair(pairs, 'encrypt')
print("Encrypted Text:", encrypted)

dec_pairs = [encrypted[i:i+2] for i in range(0,len(encrypted),2)]
decrypted = playfair(dec_pairs, 'decrypt')
print("Decrypted Text:", decrypted)
