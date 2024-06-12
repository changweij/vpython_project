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
dt = 0.0001
g = 9.8

#f1: y = -x + 50
#    y' = -1
#    angle = atan(-y') = atan(1)

angle1 = atan(1) 
while True:

    rate(5000)

    ball1.v += vector(g * sin(angle1) * cos(angle1), -g * sin(angle1) * sin(angle1), 0) * dt
    ball1.pos.x += ball1.v.x * dt
    ball1.pos.y += ball1.v.y * dt
    
    if(ball1.pos.x >= 50):
        break


#f2: y = 0.02(x - 50)^2 - 50 = 0.02x^2 - 2x
#    y' = 0.04x - 2
#    angle = atan(-y') = atan(2 - 0.04x)

t = 0
time = 0
vt = 0
at = 0
while True:
    rate(5000)
    
    slope = 2 - 0.04 * ball2.pos.x
    
    ball2.a = vector(g * (slope / (1 + slope * slope)), -g * (slope * slope / (1 + slope * slope)), 0)
    ball2.v += ball2.a * dt
    ball2.pos.x += ball2.v.x * dt
    ball2.pos.y = 0.02 * (ball2.pos.x - 50)**2 - 50
    
    at = g * (slope / sqrt(1 + slope * slope))
    vt += at * dt
    ball3.v.x = vt * (1 / sqrt(1 + slope * slope))
    ball3.v.y = -vt * (slope / sqrt(1 + slope * slope))
    ball3.pos.x += ball3.v.x * dt
    ball3.pos.y += ball3.v.y * dt
    
    
    
    time += 10 * dt
    print(ball2.a.x)
    print(ball2.a.y)
    
    if(ball2.pos.x >= 50):
        break
