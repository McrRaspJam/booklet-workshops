import string

# input plaintext
plaintext = input("Enter plaintext: ")
shift = int(input("Enter shift (positive=right): "))
ciphertext = ""

alphabet = list(string.ascii_lowercase)
subalphabet = []

# generate substitute alphabet
for letter in alphabet:
        charnum = ord(letter) - 97
        charnum = (charnum + shift) % 26
        subalphabet.append(alphabet[charnum])

# perform the cipher
for letter in plaintext:
    charnumber = ord(letter) - 97
    ciphertext += subalphabet[charnumber]

print (ciphertext)
