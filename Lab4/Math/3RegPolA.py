import math

sides = int(input('Input your number of sides: '))
length = int(input('Input your length: '))

perimetr = length * sides
apothem = (length / (2 * math.tan(math.radians(180 / sides))))
area = int((perimetr * apothem) / 2)

print(f'Your area: {area}')