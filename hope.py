from vpython import *
g = 9.8 # g = 9.8 m/s^2
size = 0.25 # ball radius = 0.25 m
height = 15 # ball center initial height = 15 m
m0 = 10
m1 = 10
m2 = 10
k1 = 1
k2 = 1
scene = canvas(width = 800, height = 800, center = vec(0,height/2,0), background=vec(0.5,0.5,0)) # open a window
floor = box(length=30, height=0.01, width=10, color=color.blue) # the floor
ball_0 = sphere(pos = vec( -10, height, 0), radius = size, color=color.red, make_trail = True, trail_radius = 0.05) # the ball
ball_1 = sphere(pos = vec( 0, height, 0), radius = size, color=color.green, make_trail = True, trail_radius = 0.05) # the ball
ball_2 = sphere(pos = vec( 10, height, 0), radius = size, color=color.blue, make_trail = True, trail_radius = 0.05) # the ball
#msg = text(text = 'Free Fall', pos = vec(-10, 10, 0))

ball_0.v = vec(0, 0, 0) # ball initial velocity
ball_1.v = vec(0, 0, 0) # ball initial velocity
ball_2.v = vec(100, 0, 0) # ball initial velocity

ball_0.a = vec(0, 0, 0) # ball initial acceleration
ball_1.a = vec(0, 0, 0) # ball initial acceleration
ball_2.a = vec(0, 0, 0) # ball initial acceleration
dt = 0.001 # time step

# original length of the strings : 10m

t = 0
while True: 
    
    rate(1000) # run 1000 times per real second
    
    
    ball_0.a = k1 * (ball_1.pos.x - ball_0.pos.x - 10) / m0
    ball_1.a = -k1 * (ball_1.pos.x - ball_0.pos.x - 10) / m1 + k2 * (ball_2.pos.x - ball_1.pos.x - 10) / m1
    ball_2.a = -k2 * (ball_2.pos.x - ball_1.pos.x - 10) / m2
    
    ball_0.v += ball_0.a * dt
    ball_1.v += ball_1.a * dt
    ball_2.v += ball_2.a * dt
    
    ball_0.pos += ball_0.v * dt
    ball_1.pos += ball_1.v * dt
    ball_2.pos += ball_2.v * dt
    


    
#msg.visible = False
#msg = text(text = str(ball.v.y), pos = vec(-10, 10, 0))
#print(ball.v.y)
