"""
Maayan Eliya
-method that get 2 matrices and return a matrix the matrix contain max size with the addition of the matrices.
"""

import numpy as np

def max_add (arr1,arr2):
    a2=arr2.shape
    a1=arr1.shape
    nr= max(a1[0],a2[0])
    nc= max(a1[1],a2[1])
    res=np.zeros((nr,nc))
    for row in range(a1[0]):
        for column in range(a1[1]):
            res[row][column] += arr1[row][column]
    for row in range(a2[0]):
        for column in range(a2[1]):
            res[row][column] += arr2[row][column]
    return res
    
    
def main():
    arr1=np.array([[1,2],[4 ,5],[6,7]])
    arr2=np.array([[7,8,9,10],[11,12,13,14]])
    max_res=max_add(arr1,arr2)
    print(max_res)


if __name__ == '__main__':
    main()

