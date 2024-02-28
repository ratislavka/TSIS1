import re

# Your string
s = input()

# Use regex to split the string at uppercase letters
split_string = re.split('(?=[A-Z])', s)

# Print the split string
print(split_string)
