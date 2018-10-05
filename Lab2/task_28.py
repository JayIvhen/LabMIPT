#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    painted = 0
    while painted != 5:
        move_right()
        if cell_is_filled():
            painted += 1


if __name__ == '__main__':
    run_tasks()
