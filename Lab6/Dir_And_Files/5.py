def write_list_to_file(filename, lst):
    # Open the file
    f = open(filename, 'w')

    # Write each item in the list to the file
    for item in lst:
        f.write(str(item) + '\n')

    # Close the file
    f.close()


# Specify the filename and the list here
filename = '/Users/ratislavovc/Documents/Code/Second_Sem/Lab6/Dir_And_Files/file.txt'
lst = ['apple', 'banana', 'cherry']
write_list_to_file(filename, lst)
