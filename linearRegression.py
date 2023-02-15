import numpy as np
import matplotlib.pyplot as plt

# Original SGR: y = a*(1/(b+x))
# Linearized SGR: 1/y = (b/a)(1/x)+(1/a)

x = np.array([0.75, 2, 3, 4, 6, 8, 8.5])
y = np.array([1.2, 1.95, 2, 2.4, 2.4, 2.7, 2.6])
X = np.linspace(0,9,num=100,endpoint=True)
Y = []
muG = None
fVal = []
err = None

def findSGR(args=None):
    global Y
    for i in X:
        tmp = 2.92791*(i/(1.08134+i))
        Y.append(tmp)

def findPWR(args=None):
    global Y
    for i in X:
        tmp = 1.4233*(i**0.311422)
        Y.append(tmp)

def findQuad(args=None):
    global Y
    for i in X:
        tmp = -0.0306938*(i**2)+0.449901*i+0.990728
        Y.append(tmp)

def findR2(args=None):
    global err, muG, fVal
    muG = np.mean(y)
    for i in x:
        # fVal.append(2.92791*(i/(1.08134+i)))
        # fVal.append(1.4233*(i**0.311422))
        fVal.append(-0.0306938*(i**2)+0.449901*i+0.990728)
    SStot = np.sum(np.square(y-muG))
    SSres = np.sum(np.square(y-fVal))
    err =  1 - (SSres/SStot)
    return err


def main(args=None):
    #findSGR()
    #findPWR()
    findQuad()
    findR2()
    plt.plot(x,y,'ko',label="Original Data")
    plt.plot(X,Y,label="Modelled Data")
    plt.legend()
    tmp = 'R2 = %1.6f' % err
    plt.title(tmp)
    plt.show()
    print(err)


if __name__ == "__main__":
    main()