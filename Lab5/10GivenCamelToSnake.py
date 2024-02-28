import re

def camel_to_snake(camel_str):
    # Insert an underscore before any uppercase letter, then convert the entire string to lowercase
    snake_str = re.sub(r'([A-Z])', r'_\1', camel_str).lower()

    # Remove the leading underscore if the original string started with an uppercase letter
    if snake_str.startswith('_'):
        snake_str = snake_str[1:]

    return snake_str

# Test the function
camel_str = input()
print(camel_to_snake(camel_str))
