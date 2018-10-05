#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_9_3():

    """
    def triangle(position):
        if position == "up":
            fill_cell()
            for i in range(2):
                move_right()
                fill_cell()
            move_left()
            move_down()
            fill_cell()
            move_up()
            move_left()
        elif position == "left":
            fill_cell()
            for i in range(2):
                move_down()
                fill_cell()
            move_up()
            move_right()
            fill_cell()
            move_left()
            move_up()
        elif position == "right":
            fill_cell()
            for i in range(2):
                move_down()
               fill_cell()
            move_up()
            move_left()
            fill_cell()
            move_right()
            move_up()
        elif position == "down":
            fill_cell()
            for i in range(2):
                move_right()
                fill_cell()
            move_left()
            move_up()
            fill_cell()
            move_down()
            move_left()

    length = 1
    while not wall_is_on_the_right():
        length += 1
        move_right()
    move_left(length//2 + 1)
    triangle("up")
    while not wall_is_beneath():
        move_down()
    triangle("down")
    move_up(length//2 + 1)
    move_left()
    triangle("left")
    while not wall_is_on_the_right():
        move_right()
    triangle("right")
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()

    """

    length = 1
    while not wall_is_on_the_right():
        length += 1
        move_right()
    while length != 1:
        path = 1
        while path != length:
            path += 1
            move_down()
            for j in range(length-2):
                path += 1
                fill_cell()
                move_down()
        path = 1
        while path != length:
            path += 1
            move_left()
            for j in range(length-2):
                path += 1
                fill_cell()
                move_left()
        path = 1
        while path != length:
            path += 1
            move_up()
            for j in range(length-2):
                path += 1
                fill_cell()
                move_up()
        path = 1
        while path != length:
            path += 1
            move_right()
            for j in range(length-2):
                path += 1
                fill_cell()
                move_right()

        move_left()
        move_down()
        length -= 2

    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()


if __name__ == '__main__':
    run_tasks()
