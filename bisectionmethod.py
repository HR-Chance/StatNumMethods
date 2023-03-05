import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Here are environemental variables
Ea = 100
Es = 0.01
xus = []
xls = []
xrs = []
eas = []
evals = []
evalL = []
evalM = []
iters = []
iter = None
xl = None
xu = None
xr = None
info = None
test = None
x = None
y = []

def newVal(xVal):
    # newY = 85*xVal-91*np.power(xVal,2)+44*np.power(xVal,3)-8*np.power(xVal,4)+np.power(xVal,5)-26
    #newY = 82*xVal-90*np.power(xVal,2)+44*np.power(xVal,3)-8*np.power(xVal,4)+0.7*np.power(xVal,5)-25
    newY = np.exp(-xVal) - xVal
    return newY

def error(XR, XRO):
    global Ea
    Ea = np.abs((XR-XRO)/XR)*100

def grepData():
    global xus, xls, xrs, eas, evals, iters, evalL, evalM
    iters.append(iter)
    xus.append(xu)
    xls.append(xl)
    xrs.append(xr)
    eas.append(Ea)
    evals.append(newVal(xr))
    evalL.append(newVal(xl))
    evalM.append(test)

def mkTable():
    global info
    info = {'Iteration':iters, 'Xl':xls,'Xu':xus,'Xr':xrs,'f(xl)':evalL,'f(xr)':evals,'f(xl)f(xr)':evalM,'Ea':eas}

def mkGraph():
    global x, y
    x = np.linspace(0.4,0.6,20)
    for i in x:
        y.append(newVal(i))
    plt.plot(x,y)
    plt.axhline(y=0, c="black")
    plt.grid()
    plt.show()

def main():
    global iter, Ea, xus, xls, xrs, eas, evals, xu, xl, xr, test
    xl = 0.5
    xu = 1.0
    xr = xu
    iter = 1
    while Ea > Es:
        xro = xr
        xr = (xu+xl)/2
        error(xr,xro)
        test = newVal(xl)*newVal(xr)
        grepData()
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            Ea = 0
        iter = iter + 1

    mkGraph()
    mkTable()
    print(tabulate(info, headers='keys', tablefmt='fancy_grid'))


if __name__ == "__main__":
    main()