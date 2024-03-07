import os

def list_directories_files(path):
    # Initialize lists to store directory and file names
    directories = []
    files = []

    # Loop through each item in the directory
    for item in os.listdir(path):  # loop that iterates over each item in the directory
        # If the item is a directory, add it to the directories list
        if os.path.isdir(os.path.join(path, item)):    # checks if the path represents a directory
            directories.append(item)
        # If the item is a file, add it to the files list
        else:
            files.append(item)

    # Print the directories and files
    print("Directories:")
    for directory in directories:
        print(directory)

    print("\nFiles:")
    for file in files:
        print(file)

# Specify the path here
path = '/Users/ratislavovc/Documents/KBTU'
list_directories_files(path)
