import hashlib
S = input()

hash_object = hashlib.sha256()
hash_object.update(S.encode())
hex_dig = hash_object.hexdigest()

print(hex_dig)