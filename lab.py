# Imports
from click import getchar
from gfxhat import lcd
import camp0851Library

# Generates dictionary
def generateDictionary():
    # Saves the contents of font.txt in the varaible font and create a new dictionary
    font = open('font3.txt', 'r')
    dictionary = dict()

    # Goes through each line of font.txt, removes '\n's, and splits the string into a list where the first value is added to the dictionary as a key while the second is the valu
    for line in font:
        line = line.replace('\n', '')
        splitLine = line.split(',')
        dictionary[splitLine[1]] = splitLine[0]
    # Closes font.txt
    font.close()

    # Returns the dictionary
    return dictionary

# Gets the value returned from generateDictionary() and places it in the dictionary variable
dictionary = generateDictionary()

# Sets runProgram to True
runProgram = True

# Turns on backlight and clears the screen on the gfxhat
camp0851Library.setBacklight()
camp0851Library.clearScreen()

# Runs the program until '0' is entered
while(runProgram):
    # Asks the user for a character
    print('Enter a character! (Press \'0\' to exit!)')
    character = getchar()
    # Checks to see if the user wants to leave the program
    if character == '0':
        camp0851Library.shutdown()
        runProgram = False
    else:
        # Checks to see if the character is one of the keys in the dictionary
        if character in dictionary:
            # Asks the user for x and y coordinates
            x = input('Enter x coordinate: ')
            y = input('Enter y coordinate: ')

            # Dispalys the character onto the gfxhat
            camp0851Library.displayText(character, lcd, int(x), int(y))
        else:
            print('No bit found!')