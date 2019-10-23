def f1(x,y):
    return 1.0 - x**2.0 - y
def f1x(x,y):
    return -2.0*x
def f1y(x,y):
    return -1.0

def f2(x,y):
    return 0.7 + x - y
def f2x(x,y):
    return 1.0
def f2y(x,y):
    return -1.0

def newtonSys(f1, f1x, f1y, f2, f2x, f2y, x, y, precision):
    count = 0
    while abs((f1(x,y)*f2y(x,y) - f2(x,y)*f1y(x,y)) / (f1x(x,y)*f2y(x,y) - f2x(x,y)*f1y(x,y))) > precision or abs((f2(x,y)*f1x(x,y) - f1(x,y)*f2x(x,y)) / (f1x(x,y)*f2y(x,y) - f2x(x,y)*f1y(x,y))) > precision:
        x -= (f1(x,y)*f2y(x,y) - f2(x,y)*f1y(x,y)) / (f1x(x,y)*f2y(x,y) - f2x(x,y)*f1y(x,y))
        y -= (f2(x,y)*f1x(x,y) - f1(x,y)*f2x(x,y)) / (f1x(x,y)*f2y(x,y) - f2x(x,y)*f1y(x,y))
        count += 1
    print("x:", round(x, 4))
    print("y:", round(y, 4))
    print("iterations:", count)

    return 0

newtonSys(f1, f1x, f1y, f2, f2x, f2y, 1, 2, 0.0001)

from math import sqrt

def fx(x,y):
    return -sqrt(1-y)
def fy(x,y):
    return 0.7+x

def gx(x,y):
    return y - 0.7
def gy(x,y):
    return 1- x**2

def picardSys(funcx, funcy, x, y, precision):
    count = 0
    while abs(x-funcx(x,y)) > precision or abs(y-funcy(x,y)) > precision:
        x = funcx(x,y)
        y = funcy(x,y)
        count += 1
    print("x:",round(x,4))
    print("y:",round(y,4))
    print("iterations:",count)

print("\nalinea d)")
print("first one")
picardSys(fx, fy, 0.0, 0.5, 0.00001)
print("second one")
picardSys(gx, gy, 0.0, 0.5, 0.00001)
