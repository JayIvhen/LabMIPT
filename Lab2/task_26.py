#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.005)
def task_2_4():


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


    move_right()
    for y in range(4):
        for x in range(9):
            cross()
            move_right(5)
        cross()
        move_left(35)
        move_down(4)
    for x in range(9):
        cross()
        move_right(5)
    cross()
    move_left(36)

if __name__ == '__main__':
    run_tasks()
