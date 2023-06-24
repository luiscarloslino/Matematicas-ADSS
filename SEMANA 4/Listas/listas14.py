print(' 3.1.5.3 Sorting simple lists - the bubble sort algorithm')
myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
            print(swapped)
            print(myList[i], myList[i + 1])

print("\nSorted:")
print(myList)
#  3.1.5.3 Sorting simple lists - the bubble sort algorithm
# True
# 56.0 90.0
# True
# 10.0 90.0
# True
# 10.0 56.0

# Sorted:
# [8.0, 10.0, 56.0, 90.0]
