import re

# Open the file
with open('row.txt', 'r') as file:
    data = file.read()

# Use regex to find matches
matches = re.findall('аб*', data)

# Print matches
for match in matches:
    print(match)
