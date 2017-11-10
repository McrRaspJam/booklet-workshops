import string
global plaintext

def main():
        global plaintext

        # input ciphertext
        ciphertext = input("Enter ciphertext: ")
        plaintext = ""

        alphabet = list(string.ascii_lowercase)
        subalphabet = []

        # generate substitute alphabet
        for letter in alphabet:
                charnum = ord(letter) - 97
                charnum = (charnum + shift) % 26
                subalphabet.append(alphabet[charnum])

        # perform the cipher
        for letter in ciphertext:
                charnumber = ord(letter) - 97
                plaintext += subalphabet[charnumber]

        print(plaintext)
                

def check():
        global plaintext
        return true        


if __name__ == "__main__":
        main()
