#this wont be needed,  a bigger function is easily built with the recursive function. Delete later.Not sure what this code does again but I think it prints all the letters after a parti
#particular letter. I'll update this later
testword = input("Enter word here: ")
for i in range(len(testword)):
    x1 = testword[i]
    print(testword[i + 1:])
for p in range(len(testword)):
    print(testword[:p])
