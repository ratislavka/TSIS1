import re

# Your string
s = input()

# Use regex to replace all occurrences of space, comma, or dot with a colon
s = re.sub('[ ,.]', ':', s)

# Print the modified string
print(s)
