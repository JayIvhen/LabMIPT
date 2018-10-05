#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    wall_direction = [wall_is_on_the_right, wall_is_on_the_left, wall_is_above, wall_is_beneath]
    move_direction = [move_right, move_left, move_up, move_down]
    for wall, goto in zip(wall_direction, move_direction):
        if not wall():
            go = goto
            if go == move_right:
                back = wall_is_on_the_left, move_right
            elif go == move_left:
                back = wall_is_on_the_right, move_left
            elif go == move_up:
                back = wall_is_beneath, move_up
            elif go == move_down:
                back = wall_is_above, move_down
            break
    while not wall():
        go()
    new_wall_direction = wall_direction
    new_wall_direction.remove(back[0])
    new_move_direction = move_direction
    new_move_direction.remove(back[1])
    for wall, goto in zip(new_wall_direction, new_move_direction):
        if not wall():
            go = goto
            break
    while not wall():
        go()


if __name__ == '__main__':
    run_tasks()
