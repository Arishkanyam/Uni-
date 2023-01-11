import tkinter as tk


root = tk.Tk()   
width = 520
height = 370
c = tk.Canvas(root, width=width, height=height, bg='brown3')
c.pack()
c.create_rectangle(0, height//2, width+2, height+2, fill='brown4')


class Ball:

    def __init__(self, c, x1, y1, x2, y2, radius, mass):   #color="navajowhite2"

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.radius = radius
        self.c = c
 
        #пишем формулу лобового сопротивления для определения скорости падения
        self.v = 4 #скорость
        self.F_str = 0.015 * self.v * radius     #лобовое сопротивление
        self.mass = mass      #масса
        self.Acceleration = (self.F_str / mass) * 50     #ускорение
        self.ball = c.create_oval(self.x1-self.radius, self.y1-self.radius, self.x2+self.radius, self.y2+self.radius, outline='lemonchiffon2', width=2) #fill=color
   
    #движение шаров 
    def move_ball(self):
        if c.coords(self.ball)[3] < height//2:
            c.move(self.ball, 0, self.v)
            c.after(1000//60, self.move_ball)
        elif height//2 <= c.coords(self.ball)[3] + self.F_str < height:
            c.move(self.ball, 0, self.F_str)
            c.after(1000//60, self.move_ball)
        else:
            c.move(self.ball, 0, height - c.coords(self.ball)[3])
            c.after(1000//60, self.iter_1)

    #учет инерции (прыжульки)
    def iter_1(self):
        if c.coords(self.ball)[3] - self.Acceleration >= height - self.mass*0.2:
            c.move(self.ball, 0, -self.Acceleration)
            c.after(1000//60, self.iter_1)
        elif c.coords(self.ball)[3] <= height:
            c.after(1000//60, self.iter_2)

    def iter_2(self):
        if c.coords(self.ball)[3] + self.Acceleration < height:
            c.move(self.ball, 0, self.Acceleration)
            c.after(1000//60, self.iter_2)
        else:
            c.move(self.ball, 0, height - c.coords(self.ball)[3])
            c.after(1000//60, self.iter_3)

    def iter_3(self):
        if c.coords(self.ball)[3] - self.Acceleration >= height - self.mass*0.1:
            c.move(self.ball, 0, -self.Acceleration)
            c.after(1000//60, self.iter_3)
        else:
            c.after(1000//60, self.iter_stop)

    def iter_stop(self):
        if c.coords(self.ball)[3] + self.Acceleration < height:
            c.move(self.ball, 0, self.Acceleration)
            c.after(1000//60, self.iter_stop)

        else:
            # Конечная координата частицы равна height
            c.move(self.ball, 0, height - c.coords(self.ball)[3])


ball1 = Ball(c, 50, 20, 50, 20, 40, 60)     #creation of all these balls
ball1.move_ball()

ball2 = Ball(c, 140, 20, 140, 20, 25, 50)
ball2.move_ball()

ball3 = Ball(c, 250, 20, 250, 20, 36, 75)
ball3.move_ball()

ball4 = Ball(c, 250, 20, 250, 20, 20, 40)
ball4.move_ball()

ball5 = Ball(c, 400, 20, 400, 20, 15, 10)
ball5.move_ball()

ball6 = Ball(c, 450, 20, 450, 20, 25, 30)
ball6.move_ball()


root.mainloop()