##import hashlib
##text=input("enter test")
##hash_result=hashlib.sha256(text.encode()).hexdigest()
##print("SHA256:",hash_result)

size = int(input("Enter size of hash table: "))
key = int(input("Enter key to hash: "))
hashed_value = key % size
print(f"Hashed value of {key} is {hashed_value}")



