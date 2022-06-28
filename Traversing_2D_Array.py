import numpy as np

twoDArray = np.array([[11, 12, 13, 14],
                      [21, 22, 23, 24],
                      [31, 32, 33, 34],
                      [41, 42, 43, 44],])

def traverse2dArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
        print("Next row")

traverse2dArray(twoDArray)