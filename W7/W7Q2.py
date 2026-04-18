###Blowfish Encryption/Decryption
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

print("\n--- 2. Blowfish Algorithm ---")
plaintext = input("Enter text to encrypt (Blowfish): ").encode()
key_blowfish = input("Enter key for Blowfish (8-56 chars): ").encode()

cipher = Blowfish.new(key_blowfish, Blowfish.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, Blowfish.block_size))
print("Ciphertext (hex):", ciphertext.hex())

decipher = Blowfish.new(key_blowfish, Blowfish.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), Blowfish.block_size)
print("Decrypted text:", decrypted.decode())
