
def is_palindrome(valuetotest):
    nc = str(valuetotest)
    ncfw = nc[0: len(valuetotest)]
    ncbw = nc[0: len(valuetotest)][::-1]

    #print("printing string forward", ncfw)
    #print("printing string backward", ncbw)
    return ncfw == ncbw

