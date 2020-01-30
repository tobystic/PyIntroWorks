import numpy as np

a = np.array([2,3,4])


print(a)


b = np.arange(1, 12, 2)
print(b)

c = np.linspace(1, 18, 6)

print(c.reshape(3, 2))
print("")

d = c.reshape(2, 3)
print(d)
print(c.size)

print(d.itemsize)
