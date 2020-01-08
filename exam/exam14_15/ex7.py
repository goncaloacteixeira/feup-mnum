from math import sin


def function(x):
    return x ** 3 - 10 * sin(x) + 2.8


def bissec(a, b, f, iterations=2):
    print("Iteration 0")
    print("a: %.05f" % a)
    print("b: %.05f\n" % b)

    for i in range(1, iterations + 1):
        m = (b + a) / 2.0
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
        print("Iteration", i)
        print("a: %.05f" % a)
        print("b: %.05f\n" % b)

    return a, b


if __name__ == "__main__":
    a, b = bissec(1.5, 4.2, function)
    print("Result: %.04f" % b)
