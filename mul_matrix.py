"""
Maayan Eliya
-method that get 2 matrices and return a matrix contains their multiple.
"""

import numpy as np

def mathmul (arr1, arr2):
    numOfRows = arr1.shape[0]
    numOfColumns = arr2.shape[1]
    res=np.zeros((numOfRows,numOfColumns))
    for row in range(numOfRows): # go through the rows of array1
        for column in range(numOfColumns): # go through the columns of array2
            for m in range(arr2.shape[0]): # go through the rows of array2
                res[row][column] += arr1[row][m] * arr2[m][column]
    return res


def main():

    arr1=np.array([[1,0],[0,1]])
    arr2=np.array([[4,1],[2,2]])
    res=mathmul(arr1,arr2)
    print(res)


if __name__ == '__main__':
    main()