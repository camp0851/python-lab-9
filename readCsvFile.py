# Imports the os module
import os

# Asks the user for the name of the CSV file
fileName = input('Enter the name of the CSV file: ')

# Checks to see if the CSV file exists. If it doesn't, it will tell the user the file wasn't found
if os.path.exists(fileName):
    # Creates a new list names csvList and opens the csv file to the variable csv
    csvList = []
    csv = open(fileName, 'r')

    # Loops through every line in csv file in order to add each line the csvList
    for line in csv:
        csvList.append(line)
    # Loops through every value in csvList and prints each value to the screen
    for value in csvList:
        print(value)
    
    # Closes the csv file
    csv.close()
else:
    print('File not found!')