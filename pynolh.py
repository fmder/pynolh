
import argparse
import math

import numpy

def nolh(conf, remove=None):
    """Constructs a Nearly Orthogonal Latin Hypercube (NOLH) of order *m* from
    a configuration vector *conf*. The configuration vector may contain either
    the numbers in $[0 q-1]$ or $[1 q]$ where $q = 2^{m-1}$. The columns to be
    *removed* are also in $[0 d-1]$ or $[1 d]$ where $d = m + \binom{m-1}{2}$
    is the NOLH dimensionality.
    """
    I = numpy.identity(2, dtype=int)
    R = numpy.array(((0, 1),
                     (1, 0)), dtype=int)

    if 0 in conf:
        conf = numpy.array(conf) + 1

        if remove is not None:
            remove = numpy.array(remove) + 1


    q = len(conf)
    m = math.log(q, 2) + 1
    s = m + (math.factorial(m - 1) / (2 * math.factorial(m - 3)))
    # Factorial checks if m is an integer
    m = int(m)

    A = numpy.zeros((q, q, m - 1), dtype=int)
    for i in range(1, m):
        Ai = 1
        for j in range(1, m):
            if j < m - i:
                Ai = numpy.kron(Ai, I)
            else:
                Ai = numpy.kron(Ai, R)

        A[:, :, i-1] = Ai
    
    M = numpy.zeros((q, s), dtype=int)
    M[:, 0] = conf
    
    col = 1
    for i in range(0, m - 1):
        for j in range(i + 1, m):
            if i == 0:
                M[:, col] = numpy.dot(A[:, :, j-1], conf)
            else:
                M[:, col] = numpy.dot(A[:, :, i-1], numpy.dot(A[:, :, j-1], conf))
            col += 1

    S = numpy.ones((q, s), dtype=int)
    v = 1
    for i in range(1, m):
        for j in range(0, q):
            if j % 2**(i-1) == 0:
                v *= -1
            S[j, i] = v

    col = m
    for i in range(1, m - 1):
        for j in range(i + 1, m):
            S[:, col] = S[:, i] * S[:, j]
            col += 1

    T = M * S
    
    keep = numpy.ones(s, dtype=bool)
    if remove is not None:
        keep[numpy.array(remove) - 1] = [False] * len(remove)
    
    return (numpy.concatenate((T, numpy.zeros((1, s)), -T), axis=0)[:, keep] + 8) / (2.0 * q)

def params(dim):
    """Returns the NOLH order $m$, the required configuration length $q$
    and the number of columns to remove to obtain the desired dimensionality.
    """
    m = 3
    s = 3
    q = 2**(m-1)
    
    while s < dim:
        m += 1
        s = m + math.factorial(m - 1) / (2 * math.factorial(m - 3))
        q = 2**(m-1)

    return m, q, s - dim


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=("Compute a Nearly "
        "Orthogonal Latin hypercube from a configuration vector."))
    parser.add_argument("conf", metavar="C", type=int, nargs="+",
        help="The configuration vector given as a list N1 N2 ... Nm")
    parser.add_argument("-r", "--remove", metavar="R", type=int, nargs="+",
        help="Columns to remove as a list N1 N2 ... Nm")

    args = parser.parse_args()
    print(nolh(conf=args.conf, remove=args.remove))
