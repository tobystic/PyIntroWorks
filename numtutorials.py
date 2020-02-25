import numpy as np

#put numbers into an array
a = np.array([2,3,4])


print(a)

#print numbers between 1 and 12 with a jumpspace of 2
b = np.arange(1, 12, 2)
print(b)

c = np.linspace(1, 18, 6)

#to convert the array to 3 by 2 matrix
print(c.reshape(3, 2))
print("..")

#print 
d = c.reshape(2, 3)
print(d)
print(c.size)

print(d.itemsize)
