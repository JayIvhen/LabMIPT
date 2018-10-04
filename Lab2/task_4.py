#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    for wall, goto in zip([wall_is_on_the_right, wall_is_on_the_left,
                         wall_is_above, wall_is_beneath],
                        [move_right, move_left, move_up, move_down]
                       ):
        if not wall():
            goto()
            break


if __name__ == '__main__':
    run_tasks()
