"""
curve of minkovskiy
"""

import turtle as T

LENGTH = 2000
N = 3

def curve(len, n):
    if n == 0:
        T.forward(len)
        return
    curve(len / 8, n - 1)
    T.left(90)
    curve(len / 8, n - 1)
    T.right(90)
    curve(len / 8, n - 1)
    T.right(90)
    curve(len / 8, n - 1)
    curve(len / 8, n - 1)
    T.left(90)
    curve(len / 8, n - 1)
    T.left(90)
    curve(len / 8, n - 1)
    T.right(90)
    curve(len / 8, n - 1)

if __name__ == "__main__":
    T.speed(0)
    curve(LENGTH, N)