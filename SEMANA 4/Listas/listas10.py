print('Exercise 2')

# ¿Cuál es la salida de las sgtes lineas de código?
lst = [1, 2, 3, 4, 5]
lst2 = []
add = 0

for number in lst:
    add += number
    print(add)
    lst2.append(add)

print(lst2)
# Exercise 2
# 1
# 3
# 6
# 10
# 15
# [1, 3, 6, 10, 15]
