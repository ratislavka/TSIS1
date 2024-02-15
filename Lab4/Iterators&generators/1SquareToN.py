
n = int(input('Input your N: '))

squares = []

for x in range(2, n):
    if (x*x) <= n:
        squares.append(x*x)

print(squares)