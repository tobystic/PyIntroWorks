

def permu(listgiven):


    if len(listgiven) == 0:
        return []
    elif len(listgiven) == 1:
        return [listgiven]
    else:
        lst = []
        for i in range(len(listgiven)):
            x = listgiven[i]
            xs = listgiven[:i] + listgiven[i + 1:]
            for p in permu(xs):
                lst.append([x] + p)
        return lst

sampledata = list("cade")
print("The possible outcomes are : ")
for p in permu(sampledata):
    print(p)
