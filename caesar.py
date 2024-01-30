import sys


def encrypt(message, k):
        # (% 26) + 71
    encode = [] # empty list for encoded characters

    for i in message:
        if i.isalpha() and i.islower(): # checks if char is a letter, lowercase
            num = ord(i) # gets ascii number for the letter
            enc_letter = ((num + k - 97) % 26) + 97 # calculates encrypted ascii code
            encode.append(chr(enc_letter)) # turns ascii number into letter
        else:
            encode.append(i) # appends all other characters
    
    return "".join(encode) 

def decrypt(message, k):
    decode = []

    for i in message:
        if i.isalpha() and i.islower(): # checks if character is a letter, lowercase
            num = ord(i)
            dec_letter = ((num - k - 97) % 26) + 97 # calculates decrypted ascii code
            decode.append(chr(dec_letter)) 
        else:
            decode.append(i) # appends all other characters

    return "".join(decode) 

if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)
