## TwoFish Encryption/Decryption

from Crypto.Cipher import Twofish
plaintext_tf = input("Enter text to encrypt (TwoFish): ").encode()
key_tf = input("Enter key for TwoFish (16, 24, 32 chars): ").encode()

cipher_tf = Twofish.new(key_tf, Twofish.MODE_ECB)
ciphertext_tf = cipher_tf.encrypt(pad(plaintext_tf, Twofish.block_size))
print("Ciphertext (hex):", ciphertext_tf.hex())

decipher_tf = Twofish.new(key_tf, Twofish.MODE_ECB)
decrypted_tf = unpad(decipher_tf.decrypt(ciphertext_tf), Twofish.block_size)
print("Decrypted text:", decrypted_tf.decode())
