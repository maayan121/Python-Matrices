"""
Maayan Eliya
-do mul of matrices filter(3,3) and matrix (3,3) from (8,8) while it can
"""
import numpy as np

def check_and_do(res):
    a=make_filter()
    while(res.shape[0]>=a.shape[0] and res.shape[1]>=a.shape[1]):
        res=do_mul(res,a)
    return res
    

def do_mul (res,a):
    #res=the big matrix, a=the filter
    mul=np.zeros((res.shape[0]-2,res.shape[1]-2)) #the return matrix
    for row in range(mul.shape[0]):
        for column in range (mul.shape[1]):
            a1=np.array(res[row:row+3,column:column+3]) #the matrix size (3,3) from res for mul
            mul[row][column]=do_sum(np.dot(a1,a)) #put the sum of the mul(3,3) matrix in the matrix it should return
    print(mul)
    return mul


def do_sum (matrix):
    matrix_sum=0
    for r in range (matrix.shape[0]):
        for c in range (matrix.shape[1]):
            matrix_sum += matrix[r][c]
    return matrix_sum


def make_filter():
    a=np.random.rand(3,3)
    for row in range(a.shape[0]):
        for column in range (a.shape[1]):
             a[row][column] = (a[row][column])*5
    return a
    
    
def main():
    arr1=np.random.rand(8,8)
    for row in range(arr1.shape[0]):
        for column in range (arr1.shape[1]):
            arr1[row][column] = (arr1[row][column])*5
    a=make_filter()
    mul=do_mul (arr1,a)
    mul=check_and_do(mul)
    print("the final array is:")
    print(mul)


if __name__ == '__main__':
    main()