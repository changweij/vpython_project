from vpython import *
g = 9.8 # g = 9.8 m/s^2
size = 0.5 # ball radius = 0.25 m
height = 5 # ball center initial height = 15 m
m0 = 10
m1 = 10
m2 = 10
k1 = 1
k2 = 1
scene = canvas(width = 800, height = 800, center = vec(0,height/2,0), background=vec(0.5,0.5,0), color = color.white) # open a window
floor = box(length = 200, height = 0.01, width = 10, color = color.black) # the floor
#curve(pos=[vec(-150, height, 0), vec(500, height, 0)], color=color.white, radius=0.02)
ball_0 = sphere(pos = vec( -60, height, 0), radius = size, color=color.red) # the ball
ball_1 = sphere(pos = vec( -50, height, 0), radius = size, color=color.blue) # the ball
ball_2 = sphere(pos = vec( -40, height, 0), radius = size, color=color.yellow) # the ball
center_of_mass = arrow(pos=vec(0, height * 2, 0), axis=vec(0, -5, 0), shaftwidth = 1, color = color.green)

#msg = text(text = 'Free Fall', pos = vec(-10, 10, 0))

ball_0.v = vec(0, 0, 0) # ball initial velocity
ball_1.v = vec(0, 0, 0) # ball initial velocity
ball_2.v = vec(5, 0, 0) # ball initial velocity

ball_0.a = vec(0, 0, 0) # ball initial acceleration
ball_1.a = vec(0, 0, 0) # ball initial acceleration
ball_2.a = vec(0, 0, 0) # ball initial acceleration
dt = 0.01 # time step

# original length of the strings : 10m

t = 0
for i in range (5):
    if(i == 0):
        m0 = 10
        m1 = 10
        m2 = 10
        k1 = 1
        k2 = 1
        
        ball_0.pos = vec( -60, height, 0)
        ball_1.pos = vec( -50, height, 0)
        ball_2.pos = vec( -40, height, 0)
        
        ball_0.v = vec(0, 0, 0) # ball initial velocity
        ball_1.v = vec(0, 0, 0) # ball initial velocity
        ball_2.v = vec(5, 0, 0) # ball initial velocity
        
        ball_0.a = vec(0, 0, 0) # ball initial acceleration
        ball_1.a = vec(0, 0, 0) # ball initial acceleration
        ball_2.a = vec(0, 0, 0) # ball initial acceleration
        
    elif(i == 1):
        m0 = 10
        m1 = 10
        m2 = 20
        k1 = 1
        k2 = 1
        
        ball_0.pos = vec( -60, height, 0)
        ball_1.pos = vec( -50, height, 0)
        ball_2.pos = vec( -40, height, 0)
        
        ball_0.v = vec(0, 0, 0) # ball initial velocity
        ball_1.v = vec(0, 0, 0) # ball initial velocity
        ball_2.v = vec(5, 0, 0) # ball initial velocity
        
        ball_0.a = vec(0, 0, 0) # ball initial acceleration
        ball_1.a = vec(0, 0, 0) # ball initial acceleration
        ball_2.a = vec(0, 0, 0) # ball initial acceleration
        
    elif(i == 2):
        m0 = 10
        m1 = 10
        m2 = 10
        k1 = 1
        k2 = 2
        
        ball_0.pos = vec( -60, height, 0)
        ball_1.pos = vec( -50, height, 0)
        ball_2.pos = vec( -40, height, 0)
        
        ball_0.v = vec(0, 0, 0) # ball initial velocity
        ball_1.v = vec(0, 0, 0) # ball initial velocity
        ball_2.v = vec(5, 0, 0) # ball initial velocity
        
        ball_0.a = vec(0, 0, 0) # ball initial acceleration
        ball_1.a = vec(0, 0, 0) # ball initial acceleration
        ball_2.a = vec(0, 0, 0) # ball initial acceleration
    
    elif(i == 3):
        m0 = 5
        m1 = 10
        m2 = 15
        k1 = 1
        k2 = 1
        
        ball_0.pos = vec( -60, height, 0)
        ball_1.pos = vec( -50, height, 0)
        ball_2.pos = vec( -40, height, 0)
        
        ball_0.v = vec(0, 0, 0) # ball initial velocity
        ball_1.v = vec(2.5, 0, 0) # ball initial velocity
        ball_2.v = vec(5, 0, 0) # ball initial velocity
        
        ball_0.a = vec(0, 0, 0) # ball initial acceleration
        ball_1.a = vec(0, 0, 0) # ball initial acceleration
        ball_2.a = vec(0, 0, 0) # ball initial acceleration
    
    elif(i == 4):
        m0 = 10
        m1 = 10
        m2 = 10
        k1 = 1
        k2 = 2
        
        ball_0.pos = vec( -60, height, 0)
        ball_1.pos = vec( -50, height, 0)
        ball_2.pos = vec( -40, height, 0)
        
        ball_0.v = vec(0, 0, 0) # ball initial velocity
        ball_1.v = vec(2.5, 0, 0) # ball initial velocity
        ball_2.v = vec(5, 0, 0) # ball initial velocity
        
        ball_0.a = vec(0, 0, 0) # ball initial acceleration
        ball_1.a = vec(0, 0, 0) # ball initial acceleration
        ball_2.a = vec(0, 0, 0) # ball initial acceleration
        
    
    
    while True: 
        
        rate(1000) # run 1000 times per real second
        
        
        ball_0.a.x = k1 * (ball_1.pos.x - ball_0.pos.x - 10) / m0
        ball_1.a.x = -k1 * (ball_1.pos.x - ball_0.pos.x - 10) / m1 + k2 * (ball_2.pos.x - ball_1.pos.x - 10) / m1
        ball_2.a.x = -k2 * (ball_2.pos.x - ball_1.pos.x - 10) / m2
        
        ball_0.v.x += ball_0.a.x * dt
        ball_1.v.x += ball_1.a.x * dt
        ball_2.v.x += ball_2.a.x * dt
        
        ball_0.pos += ball_0.v * dt
        ball_1.pos += ball_1.v * dt
        ball_2.pos += ball_2.v * dt
        center_of_mass.pos.x = (m0 * ball_0.pos.x + m1 * ball_1.pos.x + m2 * ball_2.pos.x) / (m0 + m1 + m2)
        
        
        if(ball_1.pos.x - ball_0.pos.x <= 2 * size):
            ball_0.v.x = ball_0.v.x * (m0 - m1) / (m0 + m1) + ball_1.v.x * (2 * m1) / (m0 + m1)
            ball_1.v.x = ball_1.v.x * (m1 - m0) / (m0 + m1) + ball_0.v.x * (2 * m0) / (m0 + m1)
            
        if(ball_2.pos.x - ball_1.pos.x <= 2 * size):
            ball_1.v.x = ball_1.v.x * (m1 - m2) / (m1 + m2) + ball_2.v.x * (2 * m2) / (m1 + m2)
            ball_2.v.x = ball_2.v.x * (m2 - m1) / (m1 + m2) + ball_1.v.x * (2 * m1) / (m1 + m2)
        
        print(ball_1.v.x)
        
        if(ball_2.pos.x >= 100):
            break



    
#msg.visible = False
#msg = text(text = str(ball.v.y), pos = vec(-10, 10, 0))
#print(ball.v.y)
