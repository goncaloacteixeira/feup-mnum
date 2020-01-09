import sys

sys.path.insert(1, '../../all_algs')

import multidim_minimization as mm


def function(x, y):
    return 3 * x ** 2 - x * y + 11 * y + y ** 2 - 8 * x


def function_x(x, y):
    return 6 * x - y - 8


def function_y(x, y):
    return -x + 11 + 2 * y


if __name__ == "__main__":
    mm.gradient(2, 2, 30, 30, 0.5, function, function_x, function_y, N=1)
