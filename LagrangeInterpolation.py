import numpy as np

X = 4
FX = 0
x = np.array([2, 3, 5, 7])
fx = np.array([6, 19, 99, 291])
deg = None

def constructPoly(DEG):
    global FX
    for i in range(DEG+1):
        term = fx[i]
        tmpX = np.delete(x,i)
        for j in range(DEG):
            term = term * (X-tmpX[j])/(x[i]-tmpX[j])
        print(term)
        FX = FX + term   

def main(args=None):
    global deg
    deg = len(x)-1
    constructPoly(deg)
    print(FX)

if __name__ == "__main__":
    main()