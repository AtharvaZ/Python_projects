import turtle
import colorgram
import random
from turtle import Turtle, Screen

'''
rgb_color = []
colors = colorgram.extract('hir.jpeg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_color.append(rgb)
'''

screen = Screen()
screen.colormode(255)
screen.setup(width=560, height=560)



colors = [(68, 9, 38), (10, 20, 41), (158, 14, 53), (231, 145, 80), (152, 55, 81), (167, 83, 46), (234, 51, 81), (227, 80, 58), (28, 115, 139), (245, 218, 175), (245, 202, 80), (44, 181, 160), (22, 176, 189), (96, 195, 167), (42, 126, 103), (188, 142, 36), (53, 28, 17), (15, 49, 44), (117, 228, 205), (9, 87, 108), (217, 121, 150), (110, 161, 175), (147, 29, 20), (179, 232, 208), (21, 88, 77), (246, 168, 150), (242, 160, 180), (245, 191, 201), (48, 53, 101), (80, 75, 29)]


t = Turtle()


for i in range(10):
    t.teleport(-250, -250 + 50*i, fill_gap=False)
    for j in range(10):
        t.color(random.choice(colors))
        t.pendown()
        t.dot(20)
        t.penup()
        t.fd(50)


screen.exitonclick()