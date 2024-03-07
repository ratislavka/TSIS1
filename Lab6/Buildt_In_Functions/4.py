import time
import math

def delayed_square_root(number, delay):
    time.sleep(delay/1000)  # Convert milliseconds to seconds
    return math.sqrt(number)

number = 25100
delay = 2123
result = delayed_square_root(number, delay)

print(f"Square root of {number} after {delay} milliseconds is {result}")
