
va = 1
vasq = 0
for va in range(1, 101):
    vasq = vasq + va**2

vb = 1
vbp = 0
for vb in range(1, 101):
    vbp = vbp + vb
    vbsq = vbp**2

print("the difference between " + str(vasq) + " and " + str(vbsq) + " is :", vbsq - vasq)



