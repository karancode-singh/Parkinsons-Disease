import pygame as pg
import math, sys
import random
import ctypes, time
from load_api import get_probability
import numpy as np

ctypes.windll.user32.SetProcessDPIAware()

class DisplayScreen:
    def __init__(self):
        pass
    
    def display_title(self, screen, font_size, width, height):
        pg.font.init()
        myfont = pg.font.SysFont('Arial', font_size)
        
        textsurface = myfont.render("Spiral Tests for Detecting Degree of Parkinsonism", False, (0, 0, 0))
        screen.blit(textsurface,(int(width/5), int(height/2)))
        
    
class Instructions:
    def __init__(self):
        pass
    
    def display_instructions(self, screen, width, height, inst):
        screen.blit(inst, (50, 50))
        
        
        

        
class StaticTest:
    def __init__(self):
        pass
    
    def draw_spiral(self, X, Y, surface):
        
        pg.font.init()
        myfont = pg.font.SysFont('Arial', font_size)
        
        textsurface = myfont.render("Static Spiral Test (SST)", False, (0, 0, 0))
        surface.blit(textsurface,(int(X/6), int(Y/6)))
        
        x = y = 0
        r = int(X/50)
        theta = 0
        count = 0
        while count <100:
            
            
            x = int(X/2 + r*math.cos(math.pi*theta/180))
            y = int(Y/2 - r*math.sin(math.pi*theta/180))
            pg.draw.circle(surface, (0,0,0),(x,y),5)
            r+=0.1
            count+=0.05
            theta+=0.9
            

        pg.font.init()
        myfont = pg.font.SysFont('Arial', int(font_size/2))
        
        textsurface = myfont.render("Press 'r' to retry the test or 'n' to move on to the next one.", False, (0, 0, 0))
        screen.blit(textsurface,(int(width/2), int(5*height/6)))
       
        
            

class DynamicTest:
    def __init__(self):
        pass
    
    def draw_blinking_spiral(self, X, Y, surface, col):
        
        pg.font.init()
        myfont = pg.font.SysFont('Arial', font_size)
        
        textsurface = myfont.render("Dynamic Spiral Test (DST)", False, (0, 0, 0))
        surface.blit(textsurface,(int(X/6), int(Y/6)))
        x = y = 0
        r = int(X/50)
        theta = 0
        count = 0
    
        while count <100:
            
            x = int(X/2 + r*math.cos(math.pi*theta/180))
            y = int(Y/2 - r*math.sin(math.pi*theta/180))
            pg.draw.circle(surface, col,(x,y),5)
            r+=0.1
            count+=0.05
            theta+=0.9
            
        pg.font.init()
        myfont = pg.font.SysFont('Arial', int(font_size/2))
        
        textsurface = myfont.render("Press 'r' to retry the test or 'n' to move on to the next one.", False, (0, 0, 0))
        screen.blit(textsurface,(int(width/2), int(5*height/6)))
            
    
class CircleTest:
    def __init__(self):
        pass
    
    def draw_circle(self, X, Y, screen, time_rem):
        pg.font.init()
        myfont = pg.font.SysFont('Arial', font_size)
        
        textsurface = myfont.render("Stability Test on Certain Point (STCP)", False, (0, 0, 0))
        textsurface2 = myfont.render("Hold the mouse pointer inside the circle for "+str(time_rem)+ " seconds", False, (0,0,0))
        screen.blit(textsurface,(int(X/6), int(Y/6)))
        screen.blit(textsurface2, (int(X/6), int(Y/4.7)))
        pg.draw.circle(screen, (255, 0, 0), (int(X/2), int(Y/2)), 20)
        
        pg.font.init()
        myfont = pg.font.SysFont('Arial', int(font_size/2))
        
        textsurface = myfont.render("Press 'r' to retry the test or 'n' to move on to the next one.", False, (0, 0, 0))
        screen.blit(textsurface,(int(width/2), int(5*height/6)))
    

        
class DisplayResult:
    def __init__(self):
        pass
    
    def display_result(self, res, screen, font_size, width, height):
        pg.font.init()
        myfont = pg.font.SysFont('Arial', font_size)
        
        textsurface = myfont.render(res, False, (0, 0, 0))
        screen.blit(textsurface,(int(width/4), int(height/2)))
        
class GetSpiralVals:
    def __init__(self):
        pass
    
    def user_drawn_spiral(self, screen, vals, xy):
        mouse_pos = pg.mouse.get_pos()
        xy.append(mouse_pos)
        if len(xy)==0:
            xy.append(mouse_pos)
            xy.append(mouse_pos)
            temp = list(mouse_pos)
            temp.append(0)
            temp.append(int(time.time()))
            vals.append(temp)
            vals.append(temp)
        
        pg.draw.lines(screen, (0,0,255), False, xy,4)
        mouse_pos = list(mouse_pos)
        mouse_pos.append(0)
        mouse_pos.append(int(time.time()))
        vals.append(mouse_pos)
        return vals, xy

        

def get_result(static_vals, dynamic_vals, circle_vals):
    
#     print("Static Vals:",static_vals)
#     X = []
#     Y = []
#     Z = []
#     T = []
#     for data in static_vals:
#         X.append(data[0])
#         Y.append(data[1])
#         Z.append(data[2])
#         T.append(data[3])
        
#     for data in dynamic_vals:
#         X.append(data[0])
#         Y.append(data[1])
#         Z.append(data[2])
#         T.append(data[3])
    
#     for data in circle_vals:
#         X.append(data[0])
#         Y.append(data[1])
#         Z.append(data[2])
#         T.append(data[3])
       
#     max_X = max(X)
#     max_Y = max(Y)
#     max_Z = max(Z)
#     X = np.array(X, dtype = 'float32')/max(max_X,1)
#     Y = np.array(Y, dtype = 'float32')/max(max_Y,1)
#     Z = np.array(Z, dtype = 'float32')/max(max_Z,1)
#     X = list(X)
#     Y = list(Y)
#     Z = list(Z)
    
#     print("X=",X)
    
    prob = get_probability(static_vals, dynamic_vals, circle_vals)
    res = "You exhibit " + str(prob) + "% Parkinsonian Symptoms."
    return res


pg.init()

height = 800
width  = 1400
font_size = 40

screen = pg.display.set_mode((width, height))
pg.display.set_caption("Detecting Parkinsonism")

WHITE = (255,255,255)

pg.font.init()
myfont = pg.font.SysFont('Times New Roman', 25)
inst = pg.image.load('text_image.png')



ds = DisplayScreen()
di = Instructions()
st = StaticTest()
dt = DynamicTest()
ct = CircleTest()
dr = DisplayResult()
gsv = GetSpiralVals()

mouse_pos = pg.mouse.get_pos()

static_vals = []
static_xy = []
dynamic_vals = []
dynamic_xy = []
circle_vals = []
circle_xy = []

screen_count = 0
gr = False

stt = time.time()
draw = False
col = (0,0,0)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_n:
                screen_count+=1
                draw = False
                stt = time.time()
            if event.key == pg.K_r:
                if screen_count == 2:
                    static_vals = []
                    static_xy = []
                if screen_count == 3:
                    dynamic_vals = []
                    dynamic_xy = []
                if screen_count == 4:
                    circle_vals = []
                    circle_xy = []
                    
                draw = False
                    
        if event.type == pg.MOUSEBUTTONDOWN:
            draw = True
    
    
    screen.fill(WHITE)
    if screen_count==0:
        ds.display_title(screen, font_size, width, height)
        
    if screen_count==1:
        di.display_instructions(screen, width, height, inst)
        
    if screen_count==2:
        #static spiral
        st.draw_spiral(width, height,screen)
        if draw==True:
            mouse_pos = pg.mouse.get_pos()
            static_xy.append(mouse_pos)
            mouse_pos = list(mouse_pos)
            mouse_pos.append(0)
            mouse_pos.append(int(time.time()))
            static_vals.append(mouse_pos)
            static_vals, static_xy = gsv.user_drawn_spiral(screen, static_vals, static_xy)
        
    if screen_count==3:
        #dynamic spiral
        val = random.random()
        if time.time()-stt>0.3:
            if val>0.5:
                col = (255, 255, 255)
            else:
                col = (0, 0, 0)
            stt = time.time()
        dt.draw_blinking_spiral(width, height, screen, col)
        if draw==True:
            mouse_pos = pg.mouse.get_pos()
            dynamic_xy.append(mouse_pos)
            mouse_pos = list(mouse_pos)
            mouse_pos.append(0)
            mouse_pos.append(int(time.time()))
            dynamic_vals.append(mouse_pos)
            dynamic_vals, dynamic_xy = gsv.user_drawn_spiral(screen, dynamic_vals, dynamic_xy)
        
    if screen_count==4:
        #draw circle
        time_rem = time.time() - stt
        if time_rem > 5:
            screen_count+=1
        ct.draw_circle(width, height, screen, 5 - int(time_rem))
        if draw==True:
            mouse_pos = pg.mouse.get_pos()
            circle_xy.append(mouse_pos)
            mouse_pos = list(mouse_pos)
            mouse_pos.append(0)
            mouse_pos.append(int(time.time()))
            circle_vals.append(mouse_pos)
            circle_vals, circle_xy = gsv.user_drawn_spiral(screen, circle_vals, circle_xy)
            
    if screen_count==5:
        if gr==False:
            gr = True
            res = get_result(static_vals, dynamic_vals, circle_vals)
        
        dr.display_result(res, screen, font_size, width, height)
        
    if screen_count==6:
        pg.quit()
    
    
    x,y = pg.mouse.get_pos()
    textsurface = myfont.render("X:"+str(x)+" Y:"+str(y), False, (0, 0, 0))
    
    screen.blit(textsurface,(0,0))        
    pg.display.flip()
    

