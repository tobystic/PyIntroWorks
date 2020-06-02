from checkforpalindrome import is_palindrome

#check for the highest product palindrome pair between 100 and 500 
temp = 0
for x in range(100, 450):
    for y in range(100, 500):
        z = y*x
        if is_palindrome(str(z)) and z > temp:
            temp = z
            print(temp, x, y)

