def bissection(a, b, f, iterations=10):
    print("Iteration 0")
    print("a: %.05f" % a)
    print("b: %.05f" % b)

    for i in range(1, iterations + 1):
        m = (b + a) / 2.0
        f;
        if f(a) * f(m) <= 0.0:
            b = m;
        else:
            a = m;

        print("Iteration", i)
        print("a: %.05f" % a)
        print("b: %.05f" % b)

    return a, b


def false_position(a, b, f, iterations=10):
    print("Iteration 0")
    print("a: %.05f" % a)
    print("b: %.05f" % b)

    for i in range(1, iterations + 1):
        rr = (a * f(b) - b * f(a)) / (f(b) - f(a));
        if f(a) * f(rr) <= 0.0:
            b = rr
        else:
            a = rr

        print("Iteration", i)
        print("a: %.05f" % a)
        print("b: %.05f" % b)

    return a, b


def newton(guess, f, df, iterations=10):
    print("Iteration %d: %.05f" % (0, guess))

    for i in range(1, iterations + 1):
        guess -= f(guess) / df(guess)
        print("Iteration %d: %.05f" % (i, guess))

    return guess


def picard_peano(guess,rec,iterations=10):
    print("Iteration %d: %.05f" % (0, guess))

    for i in range(1, iterations + 1):
        guess = rec(guess)
        print("Iteration %d: %.05f" % (i, guess))

    return guess



