

list = ["nyc","juno","onebox"]
list.append("yahoo")
list.append("aol")
list.append("hotmail")


print(list)
print(list[2])
print("the length of list is: " + len(list))
city = []

#pass list into an array:
for j in range(len(list)-1):
    city[j] = list[j]

print(city)

