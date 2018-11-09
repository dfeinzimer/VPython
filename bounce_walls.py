from visual import *

thickness = 0.5
side = 10
center = vector(0, 0, 0)
floor = box(pos=vector(center.x,center.y - side/2,center.z), length=side, height=thickness, width=side, color=color.blue, opacity=0.3)
ceiling = box(pos=vector(center.x,center.y + side/2,center.z), length=side, height=thickness, width=side, color=color.blue, opacity=0.3)
wall_l = box(pos=vector(center.x-side/2,center.y,center.z), length=thickness, height=side, width=side, color=color.red, opacity=0.3)
wall_r = box(pos=vector(center.x+side/2,center.y,center.z), length=thickness, height=side, width=side, color=color.red, opacity=0.3)
wall_f = box(pos=vector(center.x,center.y,center.z+side/2), length=side, height=side, width=thickness, color=color.white, opacity=0.3)
wall_b = box(pos=vector(center.x,center.y,center.z-side/2), length=side, height=side, width=thickness, color=color.white, opacity=0.3)

ball = sphere(pos=(0,1,0), color=color.red, radius=0.5)
ball.velocity=vector(2,-5,-3)

ihat = vector(1, 0, 0)
jhat = vector(0, 1, 0)
khat = vector(0, 0, 1)


def over_floor(ball, floor):
    fpos = floor.pos
    bpos = ball.pos
    fleft = fpos.x - floor.length/2
    fright = fpos.x + floor.length/2
    ffront = fpos.z + floor.width/2
    fback = fpos.z - floor.width/2
    return (fleft <= bpos.x <= fright) and (fback <= bpos.z <= ffront) 
    
dt = 0.01
counter = 0
while 1:
    rate(100)
    ball.pos += ball.velocity * dt
    if over_floor(ball, floor) and (ball.y - ball.radius <= floor.y):
        ball.velocity.y *= -1
    else:
        ball.velocity.y += -9.8*dt

    if (counter % 10 == 9):
        sphere(pos=ball.pos, color=color.yellow, radius=ball.radius/5)
#        arrow(pos=ball.pos, color=color.green, axis=ball.velocity.x*ihat, shaftwidth=0.1)
#        arrow(pos=ball.pos, color=color.green, axis=ball.velocity.y*jhat, shaftwidth=0.1)
#        arrow(pos=ball.pos, color=color.green, axis=ball.velocity.z*khat, shaftwidth=0.1)
        

    counter += 1
    if scene.mouse.clicked > 0:
        scene.mouse.getclick()
        scene.mouse.getclick()







