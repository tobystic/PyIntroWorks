## Code to list all possible permutations of a word. 

def permut(givenword):

    if len(givenword) == 0:
        return []
    elif len(givenword) == 1:
        return [givenword]
    else:
        finalarray = []
        for i in range(len(givenword)):
            x1 = givenword[i]
            #print(givenword[:i])
            x2 = givenword[:i] + givenword[i + 1:]
            for p in permut(x2):
                finalarray.append([x1] + p)
        return finalarray

sample = list("yang")
for p in permut(sample):
    print(p)
