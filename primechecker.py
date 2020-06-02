"""Code to check if a number is a prime number"""

from math import floor
from math import sqrt
from math import sin

newnumber = int(input("Enter an integer: "))

def isprime(numbertotest):

    count = 2
    numhalf = int(numbertotest/2)
    for count in range(2, numhalf+1):
        if numbertotest % count == 0:
            print("false, not a prime number")
            break
    else:
        print(newnumber, "is a prime number")



isprime(newnumber)
#print(isprime(newnumber))

#formatting answers
"""varitest = float(1500 / newnumber)
print(varitest)
print(floor(varitest))
print(sin(varitest))
print(f"The sq root of varitest is: {sqrt(varitest): 3f}")"""

