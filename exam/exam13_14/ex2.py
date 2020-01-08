from math import sqrt, cos, sin


def function(x):
    return -x + 40 * cos(sqrt(x)) + 3


def diffFunction(x):
    return - 20 * sin(sqrt(x)) / sqrt(x) - 1


def newton(guess, f, df, iterations=2):
    print("Iteration 0\nx: %.05f f(x): %.05f" % (guess, f(guess)))

    for i in range(1, iterations + 1):
        guess -= f(guess) / df(guess)
        print("Iteration %d\nx: %.05f f(x): %.05f" % (i, guess, f(guess)))

    return guess

if __name__ == "__main__":
    newton(1.7, function, diffFunction)
