
n = int(input('Input your N: '))

even = []

for x in range(n):
    if x % 2 == 0:
        even.append(x)

print(even)