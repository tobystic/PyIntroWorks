"""Code to Print List in array for prime numbers between 1 and a number"""

listofprimestocheck = (int(input("Enter an integer value: ")))

result = []

counted = 2
while counted < listofprimestocheck:

    def isPrimeNumber(numbertotest):
        count = 2
        numhalf = int(numbertotest/2)
        for count in range(2, numhalf+1):
            if numbertotest % count == 0:
                #print(counted, "is not a prime number")
                break
        else:
            #print(counted, "is a prime number")
            result.append(counted)

    isPrimeNumber(counted)
    counted += 1

print(f"The prime numbers from 1 to {listofprimestocheck} are :", result)




