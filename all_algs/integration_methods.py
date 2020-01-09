from math import sqrt


def trapezoidal_method(x0, x1, f, h=0.5):
    N = int((x1 - x0) / h)
    x = x0 + h
    res = 0
    for i in range(N - 1):
        res += f(x)
        x += h
    return h * (f(x0) + f(x1) + 2 * res) / 2


def simpson_method(x0, x1, f, h=0.5):
    res = 0
    N = int((x1 - x0) / h)
    x = x0 + h
    for i in range(1, N):
        if i % 2 == 0:
            res += 2 * f(x)
        else:
            res += 4 * f(x)
        x += h

    return h * (f(x0) + f(x1) + res) / 3


def convergence_quotient(x0, x1, f, h, method):
    s = method(x0, x1, f, h)
    s1 = method(x0, x1, f, h / 2)
    s2 = method(x0, x1, f, h / 4)

    quotient = (s1 - s) / (s2 - s1)
    order = round(sqrt(quotient))
    error = abs(s2 - s1) / (order ** 2 - 1)

    print(method.__name__)
    print("x (h=%0.06f): %0.05f" % (h, s))
    print("x (h=%0.06f): %0.05f" % (h / 2, s1))
    print("x (h=%0.06f): %0.05f" % (h / 4, s2))
    print("Quotient: %0.05f" % quotient)
    print("Error: %.08f" % error)
    print()

    return quotient
