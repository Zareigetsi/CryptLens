#caesar cipher proto

plain_text = input("string of text you want encrypted or decrypted      ")
plain_lower = plain_text.lower()

key = 3   

mode = "encrypt"

alphabet = "abcdefghijklmnopqrstuvwxyz "

encrypt_text = ''


for i in plain_lower:


    if i in alphabet:
       index = alphabet.find(i)

       if mode == "encrypt":
          encrypt_id = index + key 

       elif mode == "decrypt":
          encrypt_id = index - key
        
    
    if encrypt_id > 26:
           if encrypt_id < 29:
              encrypt_id = encrypt_id - 26
           else:
              encrypt_id = 26
           
    elif encrypt_id < 0:
           encrypt_id = encrypt_id + 26

    elif encrypt_id == 0:
             encrypt_id == 0
    
           
                                    
    encrypt_text = encrypt_text + alphabet[encrypt_id]
        


print(encrypt_text)
