# Caesar Cipher

def encrypt(text, shift):
    cipher = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                x = (ord(char) - ord('A') + shift) % 26
                cipher += chr(x + ord('A'))
            else:
                x = (ord(char) - ord('a') + shift) % 26
                cipher += chr(x + ord('a'))
        else:
            cipher += char

    return cipher


def decrypt(cipher, shift):
    plain = ""

    for char in cipher:
        if char.isalpha():
            if char.isupper():
                x = (ord(char) - ord('A') - shift) % 26
                plain += chr(x + ord('A'))
            else:
                x = (ord(char) - ord('a') - shift) % 26
                plain += chr(x + ord('a'))
        else:
            plain += char

    return plain


# -------------------------------------
#user interface

text = input("Enter text: ")
shift = int(input("Enter shift value (0-25): "))

choice = input("Encrypt (E) or Decrypt (D)? ").upper()

if choice == "E":
    encrypted = encrypt(text, shift)
    print("Encrypted:", encrypted)

elif choice == "D":
    decrypted = decrypt(text, shift)
    print("Decrypted:", decrypted)

else:
    print("Invalid choice.")