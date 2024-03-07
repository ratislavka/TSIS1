def check_all_true(tup):
    return all(tup)

# Test the function
tup = (True, True, True)
print(check_all_true(tup))  # Output: True

tup = (True, False, True)
print(check_all_true(tup))  # Output: False







'''
data = input("Enter elements: ")

# Convert the user input to a tuple of boolean values
def to_boolean(x):
    return x.lower() == 'true'

data = tuple(map(to_boolean, data.split(' ')))

# Use the all() function to check if all elements are True
result = all(data)

print(result)
'''