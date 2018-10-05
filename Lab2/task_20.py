#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    for y in range(12):
        for x in range(27):
            fill_cell()
            move_right()
        move_left(27)
        move_down()

if __name__ == '__main__':
    run_tasks()
