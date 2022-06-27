arr = [1, 2, 3, 4, 5, 6]

arr.insert(6, 7)
print("printing array: ", arr)

# accessing element
print("accessing element of array.")
def accessesElement(array, index):
    if index >= len(array):
        print("There is not any element in this index.")
    else:
        return array[index]

print(accessesElement(arr, 3))

# traverse array
print("\ntraverse array")
def traverseArray(arrays):
    for i in arrays:
        print(i)

traverseArray(arr)

# Searching element in the array
print("Searching element in the array")
def searchElement(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "does not exist"

print(searchElement(arr, 4))


# Delete Element from array
print("Deleting element")
arr.remove(3)
print(arr)

