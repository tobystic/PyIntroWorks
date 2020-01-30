
testword = input("Enter word here: ")
for i in range(len(testword)):
    x1 = testword[i]
    print(testword[i + 1:])
for p in range(len(testword)):
    print(testword[:p])