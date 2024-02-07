string = input()

def PrintPermutations(string):
    if(len(string) == 0):
        return [" "]
    perms = []
    for i in range (len(string)):
        rest = string[:i] + string[i+1:]
        for p in PrintPermutations(rest):
            perms.append(string[i] + p)
    return perms
for perms in PrintPermutations(string):
    print(perms)





