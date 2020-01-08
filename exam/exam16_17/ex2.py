def f1(x, y):
    return x ** 2 - y - 1.2


def f2(x, y):
    return -x + y ** 2 - 1.0


def f1x(x, y):
    return 2 * x


def f1y(x, y):
    return -1


def f2x(x, y):
    return -1


def f2y(x, y):
    return 2 * y


def hn(f1, f2, f1x, f1y, f2x, f2y, x, y):
    return (f1(x, y) * f2y(x, y) - f2(x, y) * f1y(x, y)) / (f1x(x, y) * f2y(x, y) - f2x(x, y) * f1y(x, y))


def kn(f1, f2, f1x, f1y, f2x, f2y, x, y):
    return (f2(x, y) * f1x(x, y) - f1(x, y) * f2x(x, y)) / (f1x(x, y) * f2y(x, y) - f2x(x, y) * f1y(x, y))


def sysNewton(f1, f2, f1x, f1y, f2x, f2y, x, y, N=20):
    print("Iteration 0")
    print("x:", x)
    print("y:", y, "\n")

    for i in range(1, N + 1):
        x_ant = x
        x -= hn(f1, f2, f1x, f1y, f2x, f2y, x, y);
        y -= kn(f1, f2, f1x, f1y, f2x, f2y, x_ant, y);
        print("Iteration", i)
        print("x: %.05f" % x)
        print("y: %.05f\n" % y)

    return x, y


if __name__ == "__main__":
    x_guess = float(input("guess x: "))
    y_guess = float(input("guess y: "))
    n = int(input("Iterations: "))

    (x_guess, y_guess) = sysNewton(f1, f2, f1x, f1y, f2x, f2y, x_guess, y_guess, n)
