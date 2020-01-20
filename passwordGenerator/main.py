from random import randint

letters = list("abcdefghijklmnopqrstuvwsyz")
numbers = list("1234567890")
symbols = list("!@#$%^&*")

def generatePasword():
    length = int(input("Password length: "))
    password = ""

    for i in range(length):
        randomList = randint(0, 2)
        randomLetter = ""

        if randomList == 0:
            randomList = letters
        elif randomList == 1:
            randomList = numbers
        elif randomList == 2:
            randomList = symbols

        randomLetter = randint(0, 1)

        if randomLetter == 0:
            randomLetter = randomList[randint(0, len(randomList) - 1)].upper()
        elif randomLetter == 1:
            randomLetter = randomList[randint(0, len(randomList) - 1)].lower()

        password += randomLetter

    print(password)

while True:
    generatePasword()