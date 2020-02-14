
### test to reverse a string, can be called if equal to return boolean true. if cw===wc

wordtotest = input("type a word(string) to get it's reversed version : ")
wordchecker = str(wordtotest)

wc = wordchecker[0: len(wordtotest)]
print(wc)
cw = wc[::-1]
print(cw)
