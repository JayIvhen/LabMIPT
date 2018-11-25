import graphics as gr

SIZE_X = 800
SIZE_Y = 800
START_X = 400
START_Y = 700
BACK_COLOR = "Green"
START_VELOCITY = gr.Point(2, 0)
START_ACCELERATION = gr.Point(0, 0)
DELAY = 0.02
RADIUS = 10

def change(point_1, point_2):
    return gr.Point(point_1.x + point_2.x,
                    point_1.y + point_2.y)


def change_for_plantes(coords, center):
    G = 2000
    diff_x = coords.x - center.x
    diff_y = coords.y - center.y
    distance_2 = (diff_x ** 2 + diff_y ** 2) ** (3 / 2)
    return gr.Point(-diff_x * G / distance_2, -diff_y * G / distance_2)


def create_circle(coords, radius, fill_color="Yellow", outline_color="Yellow"):
    circle = gr.Circle(coords, radius)
    circle.setFill(fill_color)
    circle.setOutline(outline_color)
    return circle


def create_background(size_y, size_x, background_color):
    background = gr.Rectangle(gr.Point(0, 0), gr.Point(size_x, size_y))
    background.setFill(background_color)
    return background


def check_collision(velocity, ball, radius, SIZE_X, SIZE_Y):
    if ball.getCenter().x > SIZE_X - radius:
        velocity.x = -velocity.x

    if ball.getCenter().x < 0 + radius:
        velocity.x = -velocity.x

    if ball.getCenter().y > SIZE_Y - radius:
        velocity.y = -velocity.y

    if ball.getCenter().y < 0 + radius:
        velocity.y = -velocity.y


window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
coords = gr.Point(START_X, START_Y)
center = gr.Point(SIZE_X/2, SIZE_Y/2)
velocity = START_VELOCITY
acceleration = START_ACCELERATION

ball_1 = create_circle(coords, RADIUS)
back = create_background(SIZE_X, SIZE_Y, BACK_COLOR)
back.draw(window)
ball_1.draw(window)
y = 0
flag = True

while True:

    acceleration = change_for_plantes(ball_1.getCenter(), center)
    velocity = change(velocity, acceleration)
    ball_1.move(velocity.x, velocity.y)
    check_collision(velocity, ball_1, RADIUS, SIZE_X, SIZE_Y)

    if y < ball_1.getCenter().y and flag:
        print(ball_1.getCenter().y)
        flag = False
    if y > ball_1.getCenter().y:
        flag = True
    y = ball_1.getCenter().y

    gr.time.sleep(DELAY)

window.getMouse()
window.close()