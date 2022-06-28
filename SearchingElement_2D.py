import numpy as np

twoDArray = np.array([[11, 12, 13, 14],
                      [21, 22, 23, 24],
                      [31, 32, 33, 34],
                      [41, 42, 43, 44], ])


def searchingElement(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "The value is located in index: " + str([i]) + " " + str([j])
    return "The element is not found."


print(searchingElement(twoDArray, 43))
