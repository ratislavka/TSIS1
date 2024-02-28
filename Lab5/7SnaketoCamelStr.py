import re

def to_upper(match):
    return match.group(1).upper()

# Your snake case string
s = input()

# Use regex to find matches and replace
s = re.sub('_([a-z])', to_upper, s)

print(s)
