
n = int(input('Input your N: '))

nums = []

for x in range(n):
    if (x % 3 == 0) and(x % 4 == 0):
        nums.append(x)

print(nums)