#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    move = True
    while True:
        if move or wall_is_beneath():
            move_right()
            if wall_is_beneath():
                move = False
        else:
            break


if __name__ == '__main__':
    run_tasks()
