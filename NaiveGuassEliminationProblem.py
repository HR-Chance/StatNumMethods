import numpy as np
#     [0 -3 7]      [2]
# A = [1 2 -1], B = [3]
#     [5 -2 0]      [2]

A = np.array([[0, -3, 7],[1, 2, -1],[5, -2, 0]])
B = np.array([[2],[3],[2]])
x1 = None
x2 = None
x3 = None

def sum12(val, mat):
    elem = np.array([[1,val,0],[0,1,0],[0,0,1]])
    newMat = np.matmul(elem,mat)
    return newMat

def sum13(val, mat):
    elem = np.array([[1,0,val],[0,1,0],[0,0,1]])
    newMat = np.matmul(elem,mat)
    return newMat

def sum21(val, mat):
    elem = np.array([[1,0,0],[val,1,0],[0,0,1]])
    newMat = np.matmul(elem,mat)
    return newMat

def sum23(val, mat):
    elem = np.array([[1,0,0],[0,1,val],[0,0,1]])
    newMat = np.matmul(elem,mat)
    return newMat

def sum31(val, mat):
    elem = np.array([[1,0,0],[0,1,0],[val,0,1]])
    newMat = np.matmul(elem,mat)
    return newMat

def sum32(val, mat):
    elem = np.array([[1,0,0],[0,1,0],[0,val,1]])
    newMat = np.matmul(elem,mat)
    return newMat

def swap12(mat):
    elem = np.array([[0,1,0],[1,0,0],[0,0,1]])
    newMat = np.matmul(elem,mat)
    return newMat

def swap13(mat):
    elem = np.array([[0,0,1],[0,1,0],[1,0,0]])
    newMat = np.matmul(elem,mat)
    return newMat

def swap23(mat):
    elem = np.array([[1,0,0],[0,0,1],[0,1,0]])
    newMat = np.matmul(elem,mat)
    return newMat

def mult1(val, mat):
    elem = np.array([[val,0,0],[0,1,0],[0,0,1]])
    newMat = np.matmul(elem,mat)
    return newMat

def mult2(val, mat):
    elem = np.array([[1,0,0],[0,val,0],[0,0,1]])
    newMat = np.matmul(elem,mat)
    return newMat   

def mult3(val, mat):
    elem = np.array([[1,0,0],[0,1,0],[0,0,val]])
    newMat = np.matmul(elem,mat)
    return newMat

def main(args=None):
    global A, B, x1, x2, x3
    print('intial values')
    print(A)
    print(B)
    #swap rows 1 and 3
    A = swap13(A)
    B = swap13(B)
    # multiply row 1 by 1/5
    A = mult1(0.2,A)
    B = mult1(0.2,B)
    # add -1 row 1 to row 2
    A = sum21(-1,A)
    B = sum21(-1,B)
    # multiply row 2 by 5/12
    A = mult2(5/12,A)
    B = mult2(5/12,B)
    # add 3 row 2 to row 3
    A = sum32(3,A)
    B = sum32(3,B)
    # multiply row 3 by 4/23
    A = mult3(4/23,A)
    B = mult3(4/23,B)
    print('Naive reduced values')
    print(A)
    print(B)
    # Don't Chhange following section
    x3 = B[2]/A[2,2]
    x2 = (B[1]-A[1,2]*x3)/A[1,1]
    x1 = (B[0]-A[0,1]*x2-A[0,2]*x3)/A[0,0]
    print('Finalized Values')
    print(x1,x2,x3)

if __name__ == "__main__":
    main()