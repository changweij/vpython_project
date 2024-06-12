from vpython import *

scene = canvas(background=vec(0.8, 0.8, 0.8), width=1200, height=300, center=vec(3, 0, 10), fov=0.004)


temperature_0 = 40    #攝氏度
pressure_0 = 1        #標準大氣壓(atm)
lightspeed = 1
theta_0 = 0
lamda = 4.5e-7
n_ref = 1 + (0.0000632 + (0.0295 * lamda * lamda / (146 * lamda * lamda - 1)))


curve(pos=[vec(-7, 0, 0), vec(13, 0, 0)], color=color.red, radius=0.02)
ray = sphere(pos = vec(-6, 0, 0), color = color.blue, radius = 0.01, make_trail=True)
ray.v = (lightspeed * cos(theta_0), lightspeed * sin(theta_0), 0)


dt = 0.001

state = 0
ray.prev_v = ray.v 
theta_1 = theta_0
v1 = lightspeed
v2 = lightspeed
while True:
    rate(5000)
    
    ray.pos = ray.pos + ray.v * dt
    temperature = temperature_0 - ray.pos.y * 0.0098 #在對流層中，平均上升一公尺下降0.0098度攝氏度
    pressure = pressure_0 - ray.pos.y * 0.0000011    #距地表3000米以下，平均上升一公尺約下降0.0000011atm (100pa/9m)
    
    n_air = 1 + (n_ref - 1) * pressure / (1 + (temperature - 15) * (0.0034785))
    
    v2 = lightspeed / n_air
    theta_2 = theta_1 * n_prev / n_air  
    ray.v = (v2 * cos(theta_2), v2 * sin(theta_2), 0)
    
    #update
    n_prev = n_air
    ray.prev_v = ray.v 
    theta_1 = atan(ray.v.y / ray.v.x)
