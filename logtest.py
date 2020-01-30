import math

class quadraticequation:


    def __init__(self, a,b,c):
        self._a = float(a)
        self._b = float(b)
        self._c = float(c)

        discriminant = math.sqrt(self._b**2-(4*self._a*self._c))

        root1 = float((-self._b+discriminant)/(2*self._a))

        root2 = float((-self._b-discriminant)/(2*self._a))

        #print(root1)
        #print(root2)

    def __str__(self):
        return "The answers are : " + root1 + "and" + root2


expression1 = quadraticequation(1.0, 5.0, 6.0)
print(expression1)