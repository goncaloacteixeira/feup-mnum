from math import log, exp


def function(x):
    return exp(x) - 4 * x ** 2


def rec1(x):
    return 2 * log(2 * x)


def picardPeano(guess, rec, iterations=1):
    if iterations <= 10:
        print("Iteration 0: %.05f" % guess)

    for i in range(1, iterations + 1):
        guess = rec(guess)
        if iterations <= 10:
            print("Iteration %d: %.05f" % (i, guess))

    return guess


if __name__ == "__main__":
    x = picardPeano(1.1, rec1, iterations=1)
    print("x: %.05f" % x)
    print("Residue: %.05f" % (function(x)))
