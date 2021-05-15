from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
text = bytes(input("Text to encrypt: "), 'utf-8')
encrypted_text = f.encrypt(text)

print("Encrypted text: " + str(encrypted_text))
print('''

''')
print("Key For Decrypting: " + str(key))