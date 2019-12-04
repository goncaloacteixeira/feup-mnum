from square_n_cubature import trapezoidal_rule as tp
import math


def simpson(x0, x1, f, N):
    res = 0
    N *= 2
    h = abs((x1 - x0) / N)
    x = x0 + h

    for i in range(1, N, 2):
        res += 4 * f(x)
        x += h * 2

    x = x0 + 2 * h

    for i in range(2, N, 2):
        res += 2 * f(x)
        x += h * 2

    return h * (f(x0) + f(x1) + res) / 3


def convergenceQuotient(x0, x1, f, N, method):
    s0 = method(x0, x1, f, N)
    s1 = method(x0, x1, f, N * 2)
    s2 = method(x0, x1, f, N * 4)

    order = round((s1 - s0) / (s2 - s1))

    return (s2 - s1) / (2 ** order - 1)


def exampleSimpson(compare=False):
    N = 1000
    x0 = 0
    x1 = math.pi / 2
    expected = 1

    resT = tp.trapezoidalRule(x0, x1, tp.func1, N)
    resS = simpson(x0, x1, tp.func1, N)

    if (compare):
        print("Trapezios")
        print("Resultado:", resT)
        print("Erro Obs.:", tp.erroObs(expected, resT))
        print("QC:", convergenceQuotient(x0, x1, tp.func1, N, tp.trapezoidalRule))
        print()
        exampleSimpson()
    else:
        print("Simpson")
        print("Resultado:", resS)
        print("Erro Obs.:", tp.erroObs(expected, resS))
        print("QC:", convergenceQuotient(x0, x1, tp.func1, N, simpson))
