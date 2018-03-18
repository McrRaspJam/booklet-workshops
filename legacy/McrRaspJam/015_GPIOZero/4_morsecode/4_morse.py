from gpiozero import Buzzer
from time import sleep

#Dictionary
dictionary = {" " : " ",
              "a" : ". -",
              "b" : "- . . .",
              "c" : "- . - .",
              "d" : "- . .",
              "e" : ".",
              "f" : ". . - .",
              "g" : "- - .",
              "h" : ". . . .",
              "i" : ". .",
              "j" : ". - - -",
              "k" : "- . -",
              "l" : ". - . .",
              "m" : "- -",
              "n" : "- .",
              "o" : "- - -",
              "p" : ". - - .",
              "q" : "- - . -",
              "r" : ". - .",
              "s" : ". . .",
              "t" : "-",
              "u" : ". . -",
              "v" : ". . . -",
              "w" : ". - -",
              "x" : "- . . -",
              "y" : "- . - -",
              "z" : "- - . ."}


#Phrase Input
string = input("Enter a phrase:\t")
speed = float(input("Enter the speed (e.g. 0.25):\t"))


#Translate to Morse Code
translation = ""
for character in string:
    translation += dictionary[character]
    translation += "   "

print(translation)

#Sound the transmission
bz = Buzzer(2)

for character in translation:
    if character == ".":
        bz.on()
    elif character == "-":
        bz.on()
        sleep(speed*2)
    else:
        bz.off()

    sleep(speed)
    

