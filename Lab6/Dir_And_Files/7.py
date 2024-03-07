def copy_file(source_filename, destination_filename):
    # Open the source file in read mode
    source_file = open(source_filename, 'r')

    # Read the contents of the source file
    contents = source_file.read()

    # Close the source file
    source_file.close()

    # Open the destination file in write mode
    destination_file = open(destination_filename, 'w')

    # Write the contents to the destination file
    destination_file.write(contents)

    # Close the destination file
    destination_file.close()


# Specify the source and destination filenames here
source_filename = '/path/to/source/file.txt'
destination_filename = '/path/to/destination/file.txt'
copy_file(source_filename, destination_filename)
