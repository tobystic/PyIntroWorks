

def divisiblechecker(numbervalue):

    for varx in range(2, 11):
        if numbervalue % varx != 0:
            return False
    else:
        return True

#divisiblechecker(27)

result = 11
while result > 10:
    if divisiblechecker(result) is False:
        result += 1
    else:
        print(result)
        break
















"""def divisibleval(numberv):

    for varx in range(2, 11):
        if numberv % varx != 0:
            break
    else:
        print("true")


divisibleval(2520)"""



