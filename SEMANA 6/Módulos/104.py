# You can read about all standard Python modules here: https://docs.python.org/3/py-modindex.html.

print('5.1.4.8 Errors - the programmer')
try:
    x = int(input("Enter a number: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")

print("THE END.")

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")

print('5.1.4.10 Errors - the programmer')
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")

print('5.1.4.11 Errors - the programmer')
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")

print("THE END.")

print('5.1.5.1 The anatomy of exceptions')
# https://edube.org/learn/programming-essentials-in-python-part-2/the-anatomy-of-exceptions

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")
# 5.1.4.8 Errors - the programmer
# THE END.
# 0.09090909090909091
# THE END.
# 5.1.4.10 Errors - the programmer
# 0.2
# THE END.
# 5.1.4.11 Errors - the programmer
# You must enter an integer value.
# THE END.
# 5.1.5.1 The anatomy of exceptions
# Zero Division!
# THE END.
