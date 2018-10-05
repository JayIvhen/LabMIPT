#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.005)
def task_7_5():
    step = 1
    dist = 1
    move_right()
    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        if dist == step and not wall_is_on_the_right():
            fill_cell()
            dist = 0
            step += 1
        dist += 1




if __name__ == '__main__':
    run_tasks()
