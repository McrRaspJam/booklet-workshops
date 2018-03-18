import string

plaintext = input("Enter plaintext: ")
ciphertext = ""

alphabet = list(string.ascii_lowercase)
subalphabet = list(reversed(alphabet))

for letter in plaintext:
    charnumber = ord(letter) - 97
    ciphertext += subalphabet[charnumber]

print (ciphertext)
