# 1. Create an array and traverse

myArray = [1, 2, 3,4, 5]

for i in myArray:
    print(i)

# 2. Access individual array element
print("\nAccessing in the array")
print(myArray[2])

# 3. Append a value in the array
print("Appending element in the array")
myArray.append(6)
print(myArray)

# 4. Insert element in the array
print("Inserting element.")
myArray.insert(3, 15)
print(myArray)

# 5. Extend the array
print("Extending array")
myArray1 = [7, 8, 9, 10]
myArray.extend(myArray1)
print(myArray)

# 6. Remove items in the array
print("Removing items")
myArray.remove(15)
print(myArray)

# 7. Using pop() method to remove last element
print("Using pop to remove")
myArray.pop()
print(myArray)

# 8. Reverse the array
print("Reversing array")
myArray.reverse()
print(myArray)

# 9. Fetch any element in the array
print("Fetching element")
print(myArray.index(2))

# 10. Slice element of array
print("Slicing array")
print(myArray[1:4])
print(myArray[:4])
print(myArray[:])
print(myArray[:-1])