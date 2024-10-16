# Create the array

array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# Index
print(array[0][1]) # 2
print(array[1][2]) # 6

# Updating
array[1][2] = 7
print(array)

# Popular methods
array.append([10, 11, 12])
print(array)

array[1].remove(5)
print(array)

# Standard traversal
for i in array:
    for index in i:
        print(index, end = ", ")

# Traversal, stopping somewhere at a specific level
print("\n\n Stopping \n\n")

for i in array:
    for index in i:
        if index == 7:
            break
        print(index, end = ", ")
    




