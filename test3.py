
### test to reverse a string

wordtotest = input("type a string : ")
wordchecker = str(wordtotest)

wc = wordchecker[0: len(wordtotest)]
print(wc)
cw = wc[::-1]
print(cw)