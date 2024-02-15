
n = int(input('Input your N: '))

to0 = []

def to0(n):
    for x in range(n, -1, -1):
        yield x

for i in to0(n):
    print(i)