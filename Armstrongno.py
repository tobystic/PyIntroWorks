#####################################################################################

# Armstrong number is a number that is the sum of its own
# digits each raised to the power of the number of digits

#####################################################################################
for y in range(1000):
    u = y
    result = 0

    z = len(str(y))
    while y != 0:
        m = y % 10
        result = result + m ** z
        y = y // 10
    if result == u:
        print(result)

