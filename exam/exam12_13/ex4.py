import sys
from math import exp

sys.path.insert(1, '../../all_algs')

import integration_methods as integration



def function(x):
    return exp(1.5*x)


if __name__ == "__main__":
    integration.convergence_quotient(1,1.5,function,0.125,integration.simpson_method)

