from square_n_cubature import trapezoidal_rule as tp

def simpson(x0, x1, f, N):
    res = 0
    N *= 2
    h = abs((x1 - x0) / N)
    x = x0 + h

    for i in range(1, N, 2):
        res += 4*f(x)
        x += h*2

    x = x0 + 2*h

    for i in range(2, N, 2):
        res += 2*f(x)
        x += h*2

    return h * (f(x0) + f(x1) + res) / 3

def exampleSimpson(compare = False):
    N = 80
    x0 = 0
    x1 = 2
    expected = 8.0/3.0

    res = simpson(x0,x1,tp.func1,N)

    if (compare):
        print("Trapezios")
        print("Resultado:", res)
        print("Erro Cal.:", tp.calcErroTrap(x0, x1, tp.diffdifffunc1, N))
        print("Erro Obs.:", tp.erroObs(expected, res))
        print()
        exampleSimpson()
    else:
        print("Simpson")
        print("Resultado:", res)
        print("Erro Cal.:", tp.calcErroTrap(x0, x1, tp.diffdifffunc1, N))
        print("Erro Obs.:", tp.erroObs(expected, res))

exampleSimpson(True)

