import re

# Your string
s = input()

# Use regex to insert spaces between words starting with capital letters
s = re.sub(r'(\B[A-Z])', r' \1', s)       #\B for eliminating space in the first word    \1 to save uppercase letter

# Print the modified string
print(s)
