import os
def delete_file(path):
    # Try to open the file in read mode
    if open(path, 'r'):
        print(f"The file at {path} exists and is accessible.")

        # Try to remove the file
        if open(path, 'w'):
            print(f"The file at {path} is writable.")
            os.remove(path)
            print(f"The file at {path} has been deleted.")
        else:
            print(f"The file at {path} is not writable and cannot be deleted.")
    else:
        print(f"The file at {path} does not exist.")


# Specify the path here
path = '/path/to/file.txt'
delete_file(path)

