"""
koch snowflake
"""

import task3
import turtle as T

N = 1
LENGTH = 200

def draw_koch_snowflake(len, N):
    for i in range(3):
        task3.draw_koch(len, N)
        T.right(120)


if __name__ == "__main__":
    T.speed(0)
    draw_koch_snowflake(LENGTH, N)
