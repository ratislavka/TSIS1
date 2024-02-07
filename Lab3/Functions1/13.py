import random

print('Hello! What is your name?')

name = input()

print(f'Well,{name}, I am thinking of a number between 1 and 20.')

ran_num = random.randint(1, 20)
won = False
times = 0

while not won:
    print('Take a guess.')
    num = int(input())
    times += 1

    if num < ran_num:
        print('Your guess is too low.')
    elif num < ran_num:
        print('Your guess is too high.')
    else:
        print(f'Good job, {name}! You guessed my number in {times} guesses!')
        won = True

