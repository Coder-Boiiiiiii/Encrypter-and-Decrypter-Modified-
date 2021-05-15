from cryptography.fernet import Fernet

key = bytes(input("Key: "), 'utf-8')
text = bytes(input('Text to decrypt: '), 'utf-8')
decrypted = Fernet(key).decrypt(text)
print(decrypted)