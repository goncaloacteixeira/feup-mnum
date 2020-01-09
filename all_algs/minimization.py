def sequentialSearch(x0, func, h=1):
    a = x0
    b = a + h
    while func(a) > func(b):
        a += h
        b += h
    return [a, b]


def tercos(interval, f, prec=0.0001):
    a = interval[0]
    b = interval[1]
    while abs(b - a) > prec:
        c = a + (b - a) / 3.0
        d = b - (b - a) / 3.0
        if f(c) < f(d):
            b = d
        else:
            a = c
    return [a, b]


from math import sqrt


def aureaSec(rangeVal, f, prec=0.1):
    # B = proporção
    B = (sqrt(5) - 1) / 2

    a = rangeVal[0]
    b = rangeVal[1]

    c = a + (b - a) * B
    d = b - (b - a) * B

    fc = f(c)
    fd = f(d)

    while abs(b - a) > prec:
        if fc < fd:
            b = d
            d = c
            fd = fc
            c = a + B * (b - a)
            fc = f(c)
        else:
            a = c
            c = d
            fc = fd
            d = b - B * (b - a)
            fd = f(d)

    return [a, b]


def quadAdjust(points, f):
    x1 = points[0]
    x3 = points[1]
    x2 = (x1 + x3) / 2.0

    h = x2 - x1

    return x2 - (h * (f(x1) - f(x3))) / (2 * (f(x1) - 2 * f(x2) + f(x3)))




