from tkinter import *
import math 

root = Tk()
c = Canvas(root, width=600, height=600, bg='gray25')  #"lavender")
c.pack()

angle = 0
speed = 0.7
direction = 1 
 
ball = c.create_oval(100, 100, 500, 500, fill ='gray31')
lil_bi = c.create_oval(294,94,306, 106, fill='LightGoldenrod1') #'dark olive green'
    
 
def motion():
    global angle, direction, speed
    if angle >= 360:
        angle = 0
    else:
        x = 300 + (math.sin(math.radians(angle)) * 200)
        y = 300 - (math.cos(math.radians(angle)) * 200)#direction *
        c.coords(lil_bi, x-6, y-6, x+6, y+6)
        angle += speed
        root.after(10, motion)

    
#def motion():
#    c.move(ball, 1, 0)
#    if c.coords(ball)[2] < 300:
#        root.after(10, motion)
motion()
 
root.mainloop()