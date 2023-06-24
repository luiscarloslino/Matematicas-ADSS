print(' 3.1.4.4 Lists - collections of data | Operations on lists')
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # printing original list content

numbers[0] = 111
print("\nPrevious list content:", numbers)  # printing previous list content

numbers[1] = numbers[4]  # copying value of the fifth element to the second
print("Previous list content:", numbers)  # printing previous list content

print("\nList's length:", len(numbers))  # printing previous list length
#  3.1.4.4 Lists - collections of data | Operations on lists
# Original list content: [10, 5, 7, 2, 1]

# Previous list content: [111, 5, 7, 2, 1]
# Previous list content: [111, 1, 7, 2, 1]

# List's length: 5
