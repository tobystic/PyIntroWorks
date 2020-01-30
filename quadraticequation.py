import math


class QuadraticEquation:

    def __init__(self, a, b, c):
        self._a = float(a)
        self._b = float(b)
        self._c = float(c)

        discriminant = math.sqrt((self._b ** 2) - (4 * self._a * self._c))
        root1 = float((-self._b + discriminant) / (2 * self._a))
        root2 = float((-self._b - discriminant) / (2 * self._a))
        self._root1 = root1
        self._root2 = root2

    def __str__(self):
        return "The answers are : " + str(self._root1) + " and " + str(self._root2)


example11 = QuadraticEquation(1.0, 5.0, 6.0)
print(example11)
