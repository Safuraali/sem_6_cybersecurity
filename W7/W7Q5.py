### SHA-1 Message Digest

import hashlib
text = input("Enter text to hash: ")
hash_object = hashlib.sha1(text.encode())
message_digest = hash_object.hexdigest()
print("SHA-1 Message Digest:", message_digest)
