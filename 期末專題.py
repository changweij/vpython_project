from vpython import *

scene = canvas(background=vec(0.8, 0.8, 0.8), width=1200, height=300, center=vec(3, 0, 10), fov=0.004)



    ray = sphere(pos=vec(-6, 0.5, 0), color=color.blue, radius=0.01, make_trail=True)
    ##ray.v = 

    dt = 0.001

    state = 0

    while True:
        rate(5000)
        ray.pos = ray.pos + ray.v * dt

        