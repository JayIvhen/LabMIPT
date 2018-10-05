#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    n = 1
    for y in range(13):
        move_down()
        for x in range(n):
            move_right()
            fill_cell()
        move_left(n)
        n += 1
    move_down()
    move_right()


if __name__ == '__main__':
    run_tasks()
