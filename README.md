Python Nearly Orthogonal Latin Hypercube Generator
==================================================

This library allows to generate Nearly Orthogonal Latin Hypercubes (NOLH) according to
Cioppa (2007) and De Rainville et al. (2012) and reference therein.

Installation
------------
Clone the repository

    $ git clone http://github.com/fmder/pynolh.git

and from the cloned directory type

    $ python setup.py install

PyNOLH requires Numpy.

Usage
-----
The library contains a single generator and a function to retrieve the necessary parameters
from a desired dimensionality. To generate a 6 dimension NOLH from the indentity permutation:

    import pynolh

    dim = 6
    m, q, r = pynolh.params(dim)
    conf = range(q)
    remove = range(dim - r, dim)
    nolh = pynolh.nolh(conf, remove)

The NOLH returned is a numpy array with one row being one sample.

You can also produce a NOLH from a random permutation configuration vector and remove random columns:

    import pynolh
    import random

    dim = 6
    m, q, r = pynolh.params(dim)
    conf = random.sample(range(q), q)
    remove = random.sample(range(q), r)
    nolh = pynolh.nolh(conf, remove)

The `nolh()` function accepts configurations with either numbers in [0 q-1] or [1 q].

    import pynolh

    dim = 6
    m, q, r = pynolh.params(dim)
    conf = range(1, q + 1)
    remove = range(dim - r + 1, dim + 1)
    nolh = pynolh.nolh(conf, remove)

References
----------
Cioppa, T. M., & Lucas, T. W. (2007). Efficient nearly orthogonal and space-filling Latin hypercubes. *Technometrics*, 49(1).

De Rainville, F.-M., Gagné, C., Teytaud, O., & Laurendeau, D. (2012). Evolutionary optimization of low-discrepancy sequences. *ACM Transactions on Modeling and Computer Simulation (TOMACS)*, 22(2), 9.