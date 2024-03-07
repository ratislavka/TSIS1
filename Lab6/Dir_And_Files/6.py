# Loop over each character in the alphabet
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    # Open a new file with the current character as the name
    f = open(char + '.txt', 'w')
    # Close the file
    f.close()
