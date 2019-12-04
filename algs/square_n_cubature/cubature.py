from math import cos, sin


def function(x,y):
    return sin(x) + cos(y)


def simpsonDouble(x0,x1,y0,y1,f):
    hx = (x1-x0) / 2.0
    hy = (y1-y0) / 2.0

