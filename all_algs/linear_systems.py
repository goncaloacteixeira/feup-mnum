def sys_picard_peano(x, y, g1, g2, iterations=10):
    print("Iteration 0")
    print("x: %.05f" % x)
    print("y: %.05f\n" % y)

    for i in range(1, iterations + 1):
        x_ant = x
        x = g1(x, y)
        y = g2(x_ant, y)

        print("Iteration", i)
        print("x: %.05f" % x)
        print("y: %.05f\n" % y)

    return x, y


def hn(f1, f2, f1x, f1y, f2x, f2y, x, y):
    return (f1(x, y) * f2y(x, y) - f2(x, y) * f1y(x, y)) / (f1x(x, y) * f2y(x, y) - f2x(x, y) * f1y(x, y))


def kn(f1, f2, f1x, f1y, f2x, f2y, x, y):
    return (f2(x, y) * f1x(x, y) - f1(x, y) * f2x(x, y)) / (f1x(x, y) * f2y(x, y) - f2x(x, y) * f1y(x, y))


def sys_newton(f1, f2, f1x, f1y, f2x, f2y, x, y, iterations=10):
    print("Iteration 0")
    print("x:", x)
    print("y:", y, "\n")

    for i in range(1, iterations + 1):
        x_ant = x
        x -= hn(f1, f2, f1x, f1y, f2x, f2y, x, y)
        y -= kn(f1, f2, f1x, f1y, f2x, f2y, x_ant, y)
        print("Iteration", i)
        print("x: %.05f" % x)
        print("y: %.05f\n" % y)

    return x, y


sys_newton.__doc__ = "f1x is the partial derivative of f1 in order to x"
