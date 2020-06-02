
x = int(input("How old are you? \n"))

print("Your age is ", x)

y = ("cuppa", "capuccino", "frapuccino", "espresso" )

print(y)
print(len(y))
print(y[0])

# while x < 20:
    #print("Your recommended house type is ", houselist[1])
# while x > 20 and x < 30:
    #print("Your recommended house is ", houselist[0])
# else:
    #print("try something else or just go for ", houselist[2])



houselist = []
houselist.append("bungalow")
houselist.append("flat")
houselist.append("skyscraper")

print("The Houselisting include", houselist)
print("length", len(houselist))
print("Index 1 is", houselist[0])
print("Index 3 is ", houselist[2])

while x < 20:
    print("Your recommended house type is ", houselist[1])
while x > 20 and x < 30:
    print("Your recommended house is ", houselist[0])
else:
    print("try something else or just go for ", houselist[2])

print("Did you like your choice?")