#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.008)
def task_8_18():
    v = 0
    r = 0
    while not wall_is_on_the_right():
        if wall_is_beneath() and wall_is_above():
            if cell_is_filled():
                v += 1
                move_right()
            else:
                fill_cell()
                move_right()
        if not wall_is_above() and not wall_is_on_the_right():
            move_up()
            while not wall_is_above():
                if cell_is_filled():
                    v += 1
                    move_up()
                else:
                    fill_cell()
                    move_up()
            if cell_is_filled():
                v += 1
            else:
                fill_cell()
            while not wall_is_beneath():
                move_down()
            move_right()
    mov(r, v)


if __name__ == '__main__':
    run_tasks()
