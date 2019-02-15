#!/usr/bin/env python3

import sys

def main():
    sa = sys.argv
    assert len(sa) >= 3
    x = int(sa[1])
    y = int(sa[2])
    print(x + y * y)

if __name__ == "__main__":
    main()
