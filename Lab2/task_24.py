#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    def cross():
        fill_cell()
        move_left()
        move_down()
        fill_cell()
        for i in range(2):
            move_right()
            fill_cell()
        move_left(2)
        move_down()
        move_right()
        fill_cell()
        move_left()
        move_up(2)

    move_down()
    move_right(2)
    cross()


if __name__ == '__main__':
    run_tasks()
