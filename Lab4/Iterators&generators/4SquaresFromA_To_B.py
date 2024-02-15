import math

A = int(input('Input your A: '))
B = int(input('Input your B: '))

def squares(a, b):
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    for i in range(start, end+1):
        yield i**2

for n in squares(A, B):
    print(n)


'''import math

A = int(input('Input your A: '))
B = int(input('Input your B: '))

def squares(a, b):
    start = math.sqrt(a)
    end = math.sqrt(b)
    for i in range(start, end+1):
        yield i**2

for n in squares(A, B):
    print(n)'''
