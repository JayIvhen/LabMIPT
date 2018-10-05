#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    wall_direction = [wall_is_on_the_right, wall_is_on_the_left, wall_is_above, wall_is_beneath]
    move_direction = [move_right, move_left, move_up, move_down]
    while True:
        for wall, goto in zip(wall_direction, move_direction):
            if not wall():
                go = goto
                break
        while not wall():
            go()
            if not wall_is_above():
                break
        if not wall_is_above():
            break
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
