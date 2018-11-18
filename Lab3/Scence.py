import graphics as gr
import random

STAR_COUNT = 30
WIDTH = 700
HEIGHT = 700


def draw_background(width, height, window, color="Midnight Blue"):
    aPolygon = gr.Polygon(gr.Point(0,0), gr.Point(width, 0), gr.Point(width, height), gr.Point(0, height))
    aPolygon.setFill(color)
    aPolygon.draw(window)


def draw_sun(window, x = WIDTH, y = HEIGHT, scale = None, corner = None):
    if scale == None:
        scale = random.randint(1, 3)
    if corner == None:
        corner = random.choice((1, 2, 3, 4))
        if corner == 1:
            sun_x, sun_y = 0, 0
        elif corner == 2:
            sun_x, sun_y = x, 0
        elif corner == 3:
            sun_x, sun_y = x, y
        elif corner == 4:
            sun_x, sun_y = 0, y
    else:
        sun_x, sun_y = x, y
    circle = gr.Circle(gr.Point(sun_x, sun_y), 50*scale)
    circle.setOutline("yellow")
    circle.setFill("yellow")
    circle.draw(window)


def draw_star(x, y, window, scale = None):
    if scale == None:
        scale = random.randint(1, 3)

    line_1 = gr.Line(gr.Point(x+(6*scale), y), gr.Point(x-(6*scale), y))
    line_1.setWidth(1)
    line_1.setOutline("white")

    line_2 = gr.Line(gr.Point(x, y+(7*scale)), gr.Point(x, y-(7*scale)))
    line_2.setWidth(1)
    line_2.setOutline("white")

    line_3 = gr.Line(gr.Point(x+(4*scale), y+(4*scale)), gr.Point(x-(4*scale), y-(4*scale)))
    line_3.setWidth(1)
    line_3.setOutline("white")

    circle = gr.Circle(gr.Point(x, y), 3)
    circle.setFill('white')
    circle.setOutline('white')

    line_1.draw(window)
    line_2.draw(window)
    line_3.draw(window)
    circle.draw(window)


def draw_earth(x, y, window, scale = None, cont_points = None):
    if scale == None:
        scale = random.randint(1, 3)
    radius = 35*scale
    earth = gr.Circle(gr.Point(x, y), radius)
    earth.setFill("Cyan")

    def cont_gen(x, y, radius, cont_points_1):
        point_counter = 0
        points = []
        points.append((random.uniform(x - radius + radius/2.5, x + radius - radius/2.5), random.uniform(y - radius + radius/2.5, y + radius - radius/2.5)))
        while point_counter < round(cont_points_1*1/4):
            point_counter += 1
            point = (random.uniform(x - radius + radius/2.5 + (points[-1][0] - (x - radius + radius/2.5)), x + radius - radius/2.5), random.uniform(y - radius + radius/2.5 + (points[-1][1] - (y - radius + radius/2.5)), y + radius - radius/2.5))
            points.append(point)
            print(x)
            print(points[-1])
        while point_counter < round(cont_points_1*2/4):
            point_counter +=1
            point = (random.uniform(x - radius + radius/2.5 + (points[-1][0] - (x - radius + radius/2.5)), x + radius - radius/2.5), random.uniform(y - radius + radius/2.5, y + radius - radius/2.5 - ((y + radius - radius/2.5) - points[-1][1])))
            points.append(point)
            print(points[-1], point_counter)
        while point_counter < round(cont_points_1 * 3 / 4):
            point_counter += 1
            point = (random.uniform(x - radius + radius / 2.5, x + radius - radius/2.5 - (x + radius - radius/2.5 - points[-1][0])), random.uniform(y - radius + radius / 2.5, y + radius - radius / 2.5 - ((y + radius - radius / 2.5) - points[-1][1])))
            points.append(point)
            print(points[-1], point_counter)

        print(points)
        return points

    cont_1 = gr.Polygon([gr.Point(x, y) for x, y in cont_gen(x, y, radius, 7)])
    cont_1.setFill("brown")
    cont_1.setOutline("brown")
    cont_2 = gr.Polygon([gr.Point(x, y) for x, y in cont_gen(x, y, radius, 20)])
    cont_2.setFill("green")
    cont_2.setOutline("green")

    earth.draw(window)
    cont_2.draw(window)
    cont_1.draw(window)


window = gr.GraphWin("scence", WIDTH, HEIGHT)
draw_background(WIDTH, HEIGHT, window)
for i in range(STAR_COUNT):
    draw_star(random.randint(0, WIDTH), random.randint(0, HEIGHT), window)
draw_earth(random.randint(0, WIDTH), random.randint(0, HEIGHT), window)
draw_sun(window)
window.getMouse()
window.close()
