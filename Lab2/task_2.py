#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    move_right(2)
    move_down(2)
    if not cell_is_filled():
        fill_cell()
    move_down(1)
    move_right(2)


if __name__ == '__main__':
    run_tasks()
