"""
write factorial counting function. And make it raise error to see what recursion depth is.
"""

import sys

def fac(n):
    if n == 0:
        return 1
    return fac(n - 1)*n

print("recurion limit: ", sys.getrecursionlimit())
print(fac(-1))

