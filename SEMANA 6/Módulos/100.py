# from modulo import entidad1, entidad2, ...
from math import sin, pi

print(sin(pi/2))

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi/2))
# 1.0
# 0.99999999
