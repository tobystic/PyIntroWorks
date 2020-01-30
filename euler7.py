
def isprime(numbertotest):

    count = 2
    numhalf = int(numbertotest/2)
    for count in range(2, numhalf+1):
        if numbertotest % count == 0:
            break
    else:
        return True


result = []
counter = 2
#while count < result[7]:
for counter in range(2, 100):
    if isprime(counter):
        result.append(counter)
    else:
        counter += 1
print(result)


