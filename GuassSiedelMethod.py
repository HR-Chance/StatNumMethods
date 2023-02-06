import numpy as np
from tabulate import tabulate

A = np.array([[-8, 1, -2], [2, -6, -1], [-3, -1, 7]])
B = np.array([[-20], [-38], [-34]])
#A = np.array([[10, 2, -1], [-3, -6, 2], [1, 1, 5]])
#B = np.array([[27], [-61.5], [-21.5]])
Es = 5
Ea = 100
Eas = [100]
Ea1 = [100]
Ea2 = [100]
Ea3 = [100]
x1 = 0
x2 = 0
x3 = 0
x1s = []
x2s = []
x3s = []
xo1 = None
xo2 = None
xo3 = None
iter = 1
iters = [1]

def mkTable():
    global info
    info = {'Iteration':iters, 'X1':x1s,'X2':x2s,'X3':x3s,'Ea1':Ea1,'Ea2':Ea2,'Ea3':Ea3,'Max Ea':Eas}

def evalError(xn, xo):
    err = np.abs((xn-xo)/xn)*100
    return err

def newError(args=None):
    global Ea, Ea1, Ea2, Ea3, Eas
    tmp = np.array([evalError(x1,xo1),evalError(x2,xo2),evalError(x3,xo3)])
    Ea1.append(tmp[0])
    Ea2.append(tmp[1])
    Ea3.append(tmp[2])
    Ea = tmp.max()
    Eas.append(Ea)
    

def evalXs(args=None):
    global x1, x2, x3, xo1, xo2, xo3, x1s, x2s, x3s
    xo1 = x1
    xo2 = x2
    xo3 = x3
    x1 = (B[0]-A[0,1]*x2-A[0,2]*x3)/A[0,0]
    x2 = (B[1]-A[1,0]*x1-A[1,2]*x3)/A[1,1]
    x3 = (B[2]-A[2,0]*x1-A[2,1]*x2)/A[2,2]
    x1s.append(x1)
    x2s.append(x2)
    x3s.append(x3)

def main(args=None):
    global xo1, xo2, xo3, Ea, Ea1, Ea2, Ea3, iter, iters
    print(x1,x2,x3)
    evalXs()
    while Ea > Es:
        evalXs()
        newError()
        iter = iter + 1
        iters.append(iter)
    mkTable()
    print(tabulate(info, headers='keys', tablefmt='fancy_grid'))


if __name__ == "__main__":
    main()