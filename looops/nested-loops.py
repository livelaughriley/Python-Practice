#!/usr/bin/env python3
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def list_loop(obj: list, x: int, verbose: bool = False):
    for i in range(0, 3):
        if verbose:
            print(f"{i},  : {x} *= 10")
            x *= 10
        else:
            x *= 10
        for j in range(0, 3):
            if verbose:
                print(f"{i}, {j}: {A}{[i]}{[j]} *= {x}")
                A[i][j] *= x
            else:
                A[i][j] *= x
    return obj


ll = list_loop(A, x=1, verbose=True)
print(ll)
# list_loop(A, x=1, verbose=True)
