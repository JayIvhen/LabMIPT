#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.0005)
def task_8_30():
    flag = 0
    while True:

        if flag == 2:
            while not wall_is_on_the_left():
                move_left()
            break

        while not wall_is_beneath():
            move_down()
            flag = 0

        for go in [move_right, move_left]:
            while wall_is_beneath() and not wall_is_on_the_right() and go == move_right:
                go()
                if wall_is_on_the_right():
                    flag += 1
            while wall_is_beneath() and not wall_is_on_the_left() and go == move_left:
                go()
                if wall_is_on_the_left():
                    flag += 1



if __name__ == '__main__':
    run_tasks()
