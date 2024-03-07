
s = input()

countUp = 0
countLow = 0

for x in s:
    if x.isupper():
        countUp += 1
    else:
        countLow += 1

print(f'Upper case letters: {countUp}  Lower case letters: {countLow}')