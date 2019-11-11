# Creates the first line in the CSV files
line1 = 'Name, Count\n'

# BOYS NAMES
# Reads 2000_BoysNames.txt as well as creates 2000_BoysNames.csv
boysNamesTxt = open('2000_BoysNames.txt', 'r')
boysNamesCsv = open('2000_BoysNames.csv', 'w')

# Writes line1 onto the first line of 2000_BoysNames.csv
boysNamesCsv.write(line1)

# Goes through each line of 2000_BoysNames.txt
for name in boysNamesTxt:
    # Add a comma between the names and count in the current line
    name = name.replace(' ', ', ')
    
    # Writes the current line to 2000_BoysNames.csv
    boysNamesCsv.write(name)

# Closes boysNamesTxt and boysNamesCsv
boysNamesTxt.close()
boysNamesCsv.close()

# GIRLS NAMES
# Reads 2000_GirlsNames.txt and creates 2000_GirlsNames.csv
girlsNamesTxt = open('2000_GirlsNames.txt', 'r')
girlsNamesCsv = open('2000_GirlsNames.csv', 'w')

# Writes line1 onto the first line of 2000_GirlsNames.csv
girlsNamesCsv.write(line1)

# Goes through each line of 2000_GirlsNames.txt
for name in girlsNamesTxt:

    # Add a comma between the names and count in the current line
    name = name.replace(' ', ', ')

    # Writes the current line to 2000_GielsNames.csv
    girlsNamesCsv.write(name)

# Closes girlsNamesTxt and girlsNamesCsv
girlsNamesTxt.close()
girlsNamesCsv.close()