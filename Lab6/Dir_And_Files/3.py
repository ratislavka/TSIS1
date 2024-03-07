def check_path(path):
    # Try to open the file in read mode
    if open(path, 'r'):
        print(f"The path {path} exists.")

        # Split the path into directory and filename
        # The rsplit('/', 1) function splits the string from the right at the first occurrence of '/'.
        # The result is a list of strings (path_parts), where the first element is everything before the last '/',
        # and the second element is everything after the last '/'.
        path_parts = path.rsplit('/', 1)
        directory = path_parts[0]  # assigning the first element of the path_parts list to the variable directory
        filename = path_parts[1]   # assigning the second element of the path_parts list to the variable filename

        print(f"Directory: {directory}")
        print(f"Filename: {filename}")

# Specify the path here
path = '/Users/ratislavovc/Documents/Code/Second_Sem/Lab6/Dir_And_Files/file.txt'
check_path(path)


'''
def check_path(path):
    try:
        # Try to open the file in read mode
        f = open(path, 'r')
        print(f"The path {path} exists.")

        # Split the path into directory and filename
        path_parts = path.rsplit('/', 1)
        directory = path_parts[0]
        filename = path_parts[1]

        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
        
        
        f.close()
    except FileNotFoundError:
        print(f"The path {path} does not exist.")

# Specify the path here
path = '/Users/ratislavovc/Documents/Code/Second_Sem/Lab6/Dir_And_Files/file.txt'
check_path(path)

'''