from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

def run(frame,x,y, rad):
    rad=rad/180* math.pi
    clear_canvas()
    grass.draw(400,30)
    character.clip_composite_draw(frame*100,0,100,100 ,rad,'i',x,y,100,100)
    update_canvas()
    delay(0.05)
def run_back(frame,x,y, rad):
    rad=rad/180* math.pi
    clear_canvas()
    grass.draw(400,30)
    character.clip_composite_draw(frame*100,0,100,100 ,rad,'v',x,y,100,100)
    update_canvas()
    delay(0.05)
def run_forward(s,e):
    frame=0
    for x in range(s,e,10):
        run(frame,x,90,0)
        frame = (frame+1)%8

def run_backward():
    frame=0
    for x in range(800,0,-10):
        run(frame,x,560,180)
        frame = (frame+1)%8
def run_up():
    frame=0
    for y in range(90,600,10):
        run(frame,750,y,90)
        frame = (frame+1)%8
def run_down():
    rad=3*90/180* math.pi
    frame=0
    for y in range(600,90,-10):
        run(frame,30,y,270)
        frame = (frame+1)%8
        
def run_circle():
    frame=0
    for c in range(-90,270,2):
        x=400+250*math.cos(c/360*2*math.pi)
        y=90+250+250*math.sin(c/360*2*math.pi)
        run(frame,x,y,c+90)
        frame = (frame+1)%8

def run_leftup():
    y=90
    frame=0
    for x in range(800,400,-10):
        y=y+10*math.sin(90/360*2*math.pi)
        run_back(frame,x,y,120)
        if x==410:
            print(y)
        frame = (frame+1)%8
        
def run_leftdown():
    y=500
    frame=0
    for x in range(400,0,-10):
        y=y-10*math.sin(90/360*2*math.pi)
        run_back(frame,x,y,210)
        frame = (frame+1)%8

run_forward(400,800)
run_leftup()
run_leftdown()
run_forward(0,400)

run_forward(400,800)
run_up()
run_backward()
run_down()
run_forward(0,400)

run_circle()
    
close_canvas()
