def gradient(x0, y0, h0, f, dfx, dfy, N=20, info=True):
    x = x0
    y = y0
    h = h0

    x_list = [x]
    y_list = [y]

    if info:
        print("iteration 0")
        print("x: %.05f" % x)
        print("y: %.05f" % y)
        print("f(x,y): %.05f" % f(x, y))
        print("gradient-x: %.05f" % dfx(x,y))
        print("gradient-y: %.05f" % dfy(x,y))
        print()

    for i in range(1, N + 1):
        xn = x - dfx(x, y) * h
        yn = y - dfy(x, y) * h

        if f(xn, yn) < f(x, y):
            h *= 2
            x = xn
            y = yn
            x_list.append(x)
            y_list.append(y)
            if info:
                print("iteration",i)
                print("x: %.05f" % x)
                print("y: %.05f" % y)
                print("f(x,y): %.05f" % f(x, y))
                print("gradient-x: %.05f" % dfx(x,y))
                print("gradient-y: %.05f" % dfy(x,y))
                print()
        else:
            h /= 2

    return x, y


gradient.__doc__ = "dfx is the partial derivative of f in order to x"
