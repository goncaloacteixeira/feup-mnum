"""
    functions to operate on matrices
"""


def add(matrix1, matrix2, signal=1):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        res = []
        for i in range(len(matrix1)):
            res.append([0] * len(matrix2[0]))
            for j in range(len(matrix2[0])):
                res[i][j] = matrix1[i][j] + signal * matrix2[i][j]
    else:
        return "undefined addition"
    return res

def mult(matrix1, matrix2):
    res = []
    if len(matrix1[0]) == len(matrix2):
        for i in range(len(matrix1)):
            res.append([0] * len(matrix2[0]))
            for j in range(len(matrix2[0])):
                elem = 0
                for k in range(len(matrix2)):
                    elem += matrix1[i][k] * matrix2[k][j]
                res[i][j] = elem
    else:
        res = "no product"
    return res