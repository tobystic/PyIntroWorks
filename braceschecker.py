

def braceschecker(userword):

    wordchecker = str(userword)
    counter1 = 0
    counter2 = 0
    for i in range(len(wordchecker)):
        if wordchecker[i] == "(":
            counter1 += 1
        if wordchecker[i] == ")":
            counter2 += 1
    print(counter1, counter2)

    if counter1 == counter2:
        print("They are equal")
    else:
        print("Not balanced")


woftd = "today ( is the ( day )) that (( the Lord has ) made"
braceschecker(woftd)
