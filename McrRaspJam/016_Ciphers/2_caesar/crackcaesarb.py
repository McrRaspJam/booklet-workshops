import string

global plaintext

def main():
        global plaintext

        # input ciphertext
        ciphertext = input("Enter ciphertext: ")
        
        # Try each possible key
        for shift in range(1, 26):
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

                # Stop when the plaintext is found
                if check() == True:
                        print(plaintext)
                        break
                

def check():
        global plaintext
        found = False

        if "attack" in plaintext:
                found = True
        elif "enemy" in plaintext:
                found = True
        elif "ally" in plaintext:
                found = True
        elif "retreat" in plaintext:
                found = True

        return found
        

if __name__ == "__main__":
        main()
