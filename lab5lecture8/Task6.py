"""
Levy`s curve
"""

import turtle as T

LENGTH = 10000
N = 20

def levy_curve(len_, n):
    if n == 0:
        T.forward(len_)
        return
    T.left(45)
    levy_curve(len_ / 2, n - 1)
    T.right(90)
    levy_curve(len_ / 2, n - 1)
    T.left(45)

if __name__ == "__main__":
    T.speed(0)
    levy_curve(LENGTH, N)