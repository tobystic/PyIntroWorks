import numpy as np

data = np.arange(1, 49, 3)
data2 = np.arange(5, 60, 3)
data3 = np.random.randint(10, 50, 80)

print(data)
print("")
print(data2)
print("")
print("")

data = data.reshape(2, 8)
data2 = data.reshape(2, 8)

print(data)
print("")
print(data2)
print("")

print(data3.dtype)
print(data3.reshape(10, 8))
print("")
print("-------------------------------------------------------------------------------------------")
data4 = np.loadtxt("datafile2.txt", dtype=np.uint8, delimiter=" ")
print(data4)


