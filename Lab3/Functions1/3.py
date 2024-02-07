rabbits = 0
chickens = 0
legs = 94
heads = 35

def count_rab_chick(numlegs, numheads):
    numlegs -= numheads*2

    rabbits = numlegs/4
    chickens = numheads - rabbits

    return(chickens, rabbits)

rabbits, chickens = count_rab_chick(legs, heads)

print(f'Number of chickens: {chickens}, number of rabbits: {rabbits}')

