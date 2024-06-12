from vpython import *
import numpy as np

# 創建場景
scene = canvas(width=800, height=600, center=vector(50, -50, 0), background=color.white)

# 定義終點
x_final = 100
y_final = -100

# 創建三顆小球
ball1 = sphere(pos=vector(0, 0, 0), radius=2, color=color.red, make_trail=True)
ball2 = sphere(pos=vector(0, 0, 0), radius=2, color=color.green, make_trail=True)
ball3 = sphere(pos=vector(0, 0, 0), radius=2, color=color.blue, make_trail=True)

# 設置時間參數
t = 0
dt = 0.01

# 重力加速度
g = 9.8
