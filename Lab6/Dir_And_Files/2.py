import os

def check_path(path):
    # Check for existence
    if os.path.exists(path):
        print(f"The path {path} exists.")
    else:
        print(f"The path {path} does not exist.")
        return

    # Check for readability
    if os.access(path, os.R_OK):
        print(f"The path {path} is readable.")
    else:
        print(f"The path {path} is not readable.")

    # Check for writability
    if os.access(path, os.W_OK):
        print(f"The path {path} is writable.")
    else:
        print(f"The path {path} is not writable.")

    # Check for executability
    if os.access(path, os.X_OK):
        print(f"The path {path} is executable.")
    else:
        print(f"The path {path} is not executable.")


check_path("/Users/ratislavovc/Documents/Code/Second_Sem/Lab6/Dir_And_Files/file.txt")



