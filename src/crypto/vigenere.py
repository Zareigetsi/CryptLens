# Vigenère Cipher

'''Vigenère Cipher is a method of encrypting alphabetic text by using a series of interlinked Caesar 
ciphers based on the letters of a keyword to a text. '''

# key
def generate_key(text, key):
    key = key.upper()
    text = text.upper()

    new_key = []
    key_index = 0

    for char in text:
        if char.isalpha():
            new_key.append(key[key_index % len(key)])
            key_index += 1
        else:
            new_key.append(char)

    return "".join(new_key)

#encryption function
def encrypt(text, key):
    text = text.upper()
    key = generate_key(text, key)

    cipher = ""

    for t, k in zip(text, key):
        if t.isalpha():
            x = (ord(t) - ord('A') + ord(k) - ord('A')) % 26
            cipher += chr(x + ord('A'))
        else:
            cipher += t

    return cipher

#decryption function
def decrypt(cipher, key):
    cipher = cipher.upper()
    key = generate_key(cipher, key)

    plain = ""

    for c, k in zip(cipher, key):
        if c.isalpha():
            x = (ord(c) - ord(k)) % 26
            plain += chr(x + ord('A'))
        else:
            plain += c

    return plain

 
# -------------------------------------
#user interface

text = input("Enter text: ")
key = input("Enter key: ")

choice = input("Encrypt (E) or Decrypt (D)? ").upper()

if choice == "E":
    encrypted = encrypt(text, key)
    print("Encrypted:", encrypted)

elif choice == "D":
    decrypted = decrypt(text, key)
    print("Decrypted:", decrypted)

else:
    print("Invalid choice.")


            

    

