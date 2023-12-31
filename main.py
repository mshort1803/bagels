import random

SECRET_NUMBER_LENGTH = 3
NUMBER_OF_GUESSES = 10

def getClues(secretNumber, userGuess):
    clues = []
    
    for i in range(SECRET_NUMBER_LENGTH):
        if userGuess[i] == chosenNumber[i]:
            clues.append("Fermi")
        elif userGuess[i] in chosenNumber:
            clues.append("Pico")
        else:
            clues.append("Bagel")

    return clues

def getSecretNumber():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    chosenNumber = ""

    for i in range(SECRET_NUMBER_LENGTH):
        digit = random.choice(numbers)
        chosenNumber += str(digit)
        numbers.pop(numbers.index(digit))

    return chosenNumber

def printTitle():
    print("\n          _|_|_|      _|_|      _|_|_|  _|_|_|_|  _|")        
    print("          _|    _|  _|    _|  _|        _|        _|")        
    print("          _|_|_|    _|_|_|_|  _|  _|_|  _|_|_|    _|")        
    print("          _|    _|  _|    _|  _|    _|  _|        _|")   
    print("          _|_|_|    _|    _|    _|_|_|  _|_|_|_|  _|_|_|_|")
    print("A deductive logic game where you must guess a number based on clues")

def printInstructions():
    print("\n                          Instructions                             ")
    print("I'm thinking of a three digit number. Try to guess what it is.\n")
    print("|-----------------------------------------------------------------|")
    print("| When I say  | That means                                        |")
    print("|-----------------------------------------------------------------|")
    print("| Pico        | One digit is correct, but it's in the wrong place |")
    print("| Fermi       | One digit is correct and it's in the right place  |")
    print("| Bagel       | No digit is correct                               |")
    print("|-----------------------------------------------------------------|")

printTitle()

printInstructions()

while True:
    chosenNumber = getSecretNumber()
    print("\nI have thought of a number.\nYou have 10 guesses:")
    for guess in range(NUMBER_OF_GUESSES):
        userGuess = str(input(f"Guess {guess+1}\n"))

        if userGuess == chosenNumber:
            print("Correct!")
            break
    
        clues = getClues(chosenNumber, userGuess)

        for clue in clues:
            print(clue)

    prompt = input("Do you want to play again? (y/n)")

    if prompt != "y":
        break
        


