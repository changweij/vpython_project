from vpython import *
import numpy as np

scene = canvas(width=800, height=600, center=vector(50, -50, 0), background=color.white)

x_final = 100
y_final = -100

ball1 = sphere(pos=vector(0, 0, 0), radius=2, color=color.red, make_trail=True)
ball2 = sphere(pos=vector(0, 0, 0), radius=2, color=color.green, make_trail=True)
ball3 = sphere(pos=vector(0, 0, 0), radius=2, color=color.blue, make_trail=True)

ball1.v = vector(0, 0, 0)
ball2.v = vector(0, 0, 0)
ball3.v = vector(0, 0, 0)

t = 0
dt = 0.001
g = 9.8

while True:
    rate(1000)

    ball1.v += vector(g/2, -g/2, 0) * dt
    ball1.pos.x += ball1.v.x * dt
    ball1.pos.y += ball1.v.y * dt
