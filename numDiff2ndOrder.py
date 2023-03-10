import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

x = [0, 25, 50, 75, 100, 125]
y = [0, 32, 58, 78, 92, 100]
dy = []
ddy = []
h = 25
info  = None

def forwardVel(Y1, Y2, Y3):
    DY = (-Y1+4*Y2-3*Y3)/(2*h)
    return DY

def forwardAcc(Y1, Y2, Y3, Y4):
    DDY = (-Y1 + 4*Y2 - 5*Y3 + 2*Y4)/(h**2)
    return DDY

def centerVel(Y1, Y2):
    DY = (Y1-Y2)/(2*h)
    return DY

def centerAcc(Y1, Y2, Y3):
    DDY = (Y1 - 2*Y2 + Y3)/(h**2)
    return DDY

def backwardVel(Y1, Y2, Y3):
    DY = (3*Y1 - 4*Y2 + Y3)/(2*h)
    return DY

def backwardAcc(Y1, Y2, Y3, Y4):
    DDY = (2*Y1 - 5*Y2 + 4*Y3 - Y4)/(h**2)
    return DDY

def mkgraph(args = None):
    plt.plot(x,y,label='position')
    plt.plot(x,dy,label='velocity')
    plt.plot(x,ddy,label='acceleration')
    plt.xlabel('time')
    plt.ylabel('position')
    plt.legend()
    plt.show()

def mktable(args = None):
    global info
    info = {'x':x,'y':y,'velocity':dy,'acceleration':ddy}

def main(args=None):
    global dy, ddy
    for i in range(len(x)):
        if i == 0:
            dy.append(forwardVel(y[i+2], y[i+1], y[i]))
            ddy.append(forwardAcc(y[i+3], y[i+2], y[i+1], y[i]))
        elif i == 5:
            dy.append(backwardVel(y[i], y[i-1], y[i-2]))
            ddy.append(backwardAcc(y[i], y[i-1], y[i-2], y[i-3]))
        else:
            dy.append(centerVel(y[i+1], y[i-1]))
            ddy.append(centerAcc(y[i+1], y[i], y[i-1]))
    # mkgraph()
    mktable()
    print(tabulate(info, headers='keys', tablefmt='fancy_grid'))
    


if __name__ == "__main__":
    main()