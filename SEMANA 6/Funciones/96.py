#
print('3.1.4.9 Lists - collections of data | list methods')
myList = []  # creating an empty list

for i in range(5):
    myList.append(i + 1)

print(myList)

print(' 3.1.4.10 Lists - collections of data | lists and loops')
myList = [10, 1, 8, 3, 5]
total = 0

for i in range(len(myList)):
    total += myList[i]

print(total)
# 3.1.4.9 Lists - collections of data | list methods
# [1, 2, 3, 4, 5]
#  3.1.4.10 Lists - collections of data | lists and loops
# 27
