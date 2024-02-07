import math

radius = int(input())

'''
def volume(radius):
    pi = 3.14
    vol = (4/3)*(pi*radius*radius*radius)
    return vol
'''

def volume(radius):
    vol = (4/3)*(math.pi*radius**3)
    return vol

print(volume(radius))