
def isprime(numbertotest):

    if numbertotest < 2:
        print("Not a prime, please enter positive integers greater than or = 2 ")
    else:

        count = 2
        numhalf = int(numbertotest/2)
        for count in range(2, numhalf+1):
            if numbertotest % count == 0:
                print("false, not a prime number")
                break
        else:
            print(numbertotest, "is a prime number")


isprime(-7)
