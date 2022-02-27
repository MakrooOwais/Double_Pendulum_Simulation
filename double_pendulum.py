from p5 import *
from math import pi


global r1, r2, m1, m2
r1, r2, m1, m2 = 250, 250, 40, 40

global a1, a2
a1, a2 = [pi / 2], [pi / 2]

global v_1, v_2, acc_1, acc_2, g
v_1, v_2, acc_1, acc_2, g = [0], [0], [0], [0], [1]

global points
points = []


def setup():

    size(1000, 1000)


def draw():
    num1 = -g[0] * (2 * m1 + m2) * sin(a1[0])
    num2 = -m2 * g[0] * sin(a1[0] - 2 * a2[0])
    num3 = -2 * sin(a1[0] - a2[0]) * m2
    num4 = v_2[0] ** 2 * r2 + v_1[0] ** 2 * r1 * cos(a1[0] - a2[0])
    den = r1 * (2 * m1 + m2 - m2 * cos(2 * a1[0] - 2 * a2[0]))

    acc_1[0] = (num1 + num2 + num3 * num4) / den

    num1 = 2 * sin(a1[0] - a2[0])
    num2 = v_1[0] ** 2 * r1 * (m1 + m2)
    num3 = g[0] * (m1 + m2) * cos(a1[0])
    num4 = v_2[0] ** 2 * r2 * m2 * cos(a1[0] - a2[0])
    den = r2 * (2 * m1 + m2 - m2 * cos(2 * a1[0] - 2 * a2[0]))

    acc_2[0] = num1 * (num2 + num3 + num4) / den

    v_1[0], v_2[0] = v_1[0] + acc_1[0], v_2[0] + acc_2[0]
    a1[0] = a1[0] + v_1[0]
    a2[0] = a2[0] + v_2[0]

    background(255)
    stroke(0)
    stroke_weight(2)
    translate(500, 500)

    x1, y1 = r1 * sin(a1[0]), r1 * cos(a1[0])

    line(0, 0, x1, y1)
    fill(0)
    ellipse(x1, y1, m1, m1)

    x2, y2 = x1 + r2 * sin(a2[0]), y1 + r2 * cos(a2[0])

    line(x1, y1, x2, y2)
    fill(0)
    ellipse(x2, y2, m2, m2)

    points.append((x2, y2))
    no_fill()
    stroke(0)
    begin_shape()
    for point in points:
        curve_vertex(*point)
    end_shape()


if __name__ == "__main__":
    run()
