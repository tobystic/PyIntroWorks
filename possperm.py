### code to list all the possible arrangements of letters in a word###
### similar to number of ways 8 people may sit on a bench###

def possibleperm(newword):

    if len(newword) == 0:
        return []
    elif len(newword) == 1:
        return [newword]
    else:
        finarray = []
        for i in range(len(newword)):
            bb = newword[i]
            by = newword[:i] + newword[i + 1:]
            for p in possibleperm(by):
                finarray.append([bb] + p)
        return finarray

sampleword = list("micro")
for p in possibleperm(sampleword):
    print(p)
