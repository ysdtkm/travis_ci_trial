#!/usr/bin/env python3

import subprocess as sp
import numpy as np

def test_many():
    x, y = np.random.randint(100, size=(2,))
    z = sp.getoutput(f"python3 main.py {x} {y}")
    assert x + y == int(z)

if __name__ == "__main__":
    test_many()


