from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

def run():
    

def run_forward():
    frame=0
    for x in range(0,800,10):
        clear_canvas()
        grass.draw(400,30)
        #character.draw_now(400,30)
        character.clip_draw(frame*100,0,100,100,x,90)
        update_canvas()
        frame = (frame+1)%8
        delay(0.05)

def run_backward():
    frame=0
    for x in range(800,0,-10):
        clear_canvas()
        grass.draw(400,30)
        character.clip_composite_draw(frame*100,0,100,100 ,0,'h',x,90,100,100)
        update_canvas()
        frame = (frame+1)%8
        delay(0.05)
def run_up():
    frame=0
    for y in range(30,600,10):
        clear_canvas()
        grass.draw(400,30)
        #character.draw_now(400,30)
        character.clip_composite_draw(frame*100,0,100,100 ,90,'i',750,y,100,100)
        update_canvas()
        frame = (frame+1)%8
        delay(0.05)
def run_down():
    rad=3*90/180* math.pi
    frame=0
    for y in range(600,30,-10):
        clear_canvas()
        grass.draw(400,30)
        #character.draw_now(400,30)
        character.clip_composite_draw(frame*100,0,100,100 , rad,'i',30,y,100,100)
        update_canvas()
        frame = (frame+1)%8
        delay(0.05)


#run_forward()
#run_backward()
run_down()
    
close_canvas()
