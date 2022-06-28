# Here, we are importing numpy module because it is easy to manipulate matrix operations
import numpy as np

twoDArray = np.array([[11, 12, 13, 14],
                      [21, 22, 23, 24],
                      [31, 32, 33, 34],
                      [41, 42, 43, 44],])

print(twoDArray)
print(twoDArray[2][1])

# Inserting value in this 2D array
print("Inserting Values")

new2DArray = np.insert(twoDArray, 0, [1, 2, 3, 4], axis=1)  # if we change the axis value 1 to 0 then the value will be inserted in the row
print(new2DArray)

# Append values in the array
print("Appending values")
new_2dArray = np.append(twoDArray, [[51, 52, 53, 54], [61, 62, 63, 64]], axis=0)
print(new_2dArray)

# Delete row/column from 2D array
print("Deleting.....")
delArray = np.delete(twoDArray, 0, axis=1)
print(delArray)


# Accessing in the array
print("Accessing element in the array")
def accessElement(array, rowIdx, colIdx):
    if rowIdx >= len(array) and colIdx >= len(array[0]):
        print("Incorrect index.")
    else:
        print(array[rowIdx][colIdx])

accessElement(twoDArray, 1, 1)
