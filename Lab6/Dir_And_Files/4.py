def count_lines(filename):
    # Open the file
    f = open(filename, 'r')

    # Read the lines
    lines = f.readlines()

    # Close the file
    f.close()

    return len(lines)

# Specify the filename here
filename = '/path/to/file.txt'
print(f"The file {filename} has {count_lines(filename)} lines.")


'''
f = open("file.txt", "r")
print(f.readline())
f.close()

'''
