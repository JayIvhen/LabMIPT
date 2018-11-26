import turtle as T


def kantar(len_ , N, n=0, goto_x=0, goto_y=0):
    T.penup()
    T.goto(goto_x, goto_y)
    T.pendown()
    goto_x, goto_y = T.pos()[0], T.pos()[1]
    T.forward(len_)
    if n == N:
        return
    kantar(len_ / 3, N, n + 1, goto_x, goto_y - 40)
    kantar(len_ / 3, N, n + 1, goto_x + 2* (len_ / 3), goto_y - 40)




T.speed(0)
kantar(400, 7)