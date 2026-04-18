# ---------- TEXT PROCESSING ----------

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text]

def numbers_to_text(nums):
    return ''.join(chr(n % 26 + ord('A')) for n in nums)

def process_text(text, n):
    text = ''.join(filter(str.isalpha, text.upper()))
    while len(text) % n != 0:
        text += 'X'
    return text


# ---------- MATRIX UTILITIES ----------

def get_minor(matrix, i, j):
    return [
        [row[c] for c in range(len(matrix)) if c != j]
        for r, row in enumerate(matrix) if r != i
    ]

def determinant(matrix, mod=26):
    n = len(matrix)

    if n == 1:
        return matrix[0][0] % mod

    if n == 2:
        return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % mod

    det = 0
    for c in range(n):
        minor = get_minor(matrix, 0, c)
        sign = (-1) ** c
        det += sign * matrix[0][c] * determinant(minor, mod)

    return det % mod


def mod_inverse(a, m):
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


# ---------- MATRIX OPERATIONS ----------

def multiply_matrix_vector(matrix, vector):
    result = []
    n = len(matrix)

    for i in range(n):
        s = 0
        for j in range(n):
            s += matrix[i][j] * vector[j]
        result.append(s % 26)

    return result


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def cofactor_matrix(matrix):
    n = len(matrix)
    cof = []

    for i in range(n):
        row = []
        for j in range(n):
            minor = get_minor(matrix, i, j)
            sign = (-1) ** (i + j)
            row.append(sign * determinant(minor))
        cof.append(row)

    return cof


def inverse_matrix(matrix):
    n = len(matrix)

    det = determinant(matrix)
    inv_det = mod_inverse(det, 26)

    if inv_det is None:
        raise ValueError("Matrix not invertible mod 26")

    cof = cofactor_matrix(matrix)
    adj = transpose(cof)

    inv = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append((adj[i][j] * inv_det) % 26)
        inv.append(row)

    return inv


# ---------- ENCRYPT / DECRYPT ----------

def encrypt(text, key):
    n = len(key)
    text = process_text(text, n)

    nums = text_to_numbers(text)
    result = []

    for i in range(0, len(nums), n):
        block = nums[i:i+n]
        result.extend(multiply_matrix_vector(key, block))

    return numbers_to_text(result)


def decrypt(cipher, key):
    n = len(key)
    inv_key = inverse_matrix(key)

    nums = text_to_numbers(cipher)
    result = []

    for i in range(0, len(nums), n):
        block = nums[i:i+n]
        result.extend(multiply_matrix_vector(inv_key, block))

    return numbers_to_text(result)


# ---------- FILE HANDLING ----------

print("Hill Cipher (Variable Size Matrix)")

choice = input("1. Encrypt File\n2. Decrypt File\nEnter choice: ")

n = int(input("Enter matrix size (n x n): "))

print(f"Enter {n}x{n} key matrix:")
key = []
for i in range(n):
    key.append(list(map(int, input().split())))

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

with open(input_file, 'r') as f:
    text = f.read()

try:
    if choice == '1':
        cipher = encrypt(text, key)
        with open(output_file, 'w') as f:
            f.write(cipher)
        print("File Encrypted Successfully!")

    elif choice == '2':
        plain = decrypt(text, key)
        with open(output_file, 'w') as f:
            f.write(plain)
        print("File Decrypted Successfully!")

    else:
        print("Invalid choice!")

except Exception as e:
    print("Error:", e)
