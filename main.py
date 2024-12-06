import turtle
import math
import time
import random

class Ball:
    def __init__(self, size, x, y, vx, vy, color, id):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.mass = 100*size**2
        self.count = 0
        self.id = id
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        

    def draw(self):
        # draw a circle of radius equals to size centered at (x, y) and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y-self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def bounce_off_vertical_wall(self):
        self.vx = -self.vx
        self.count += 1

    def bounce_off_horizontal_wall(self):
        self.vy = -self.vy
        self.count += 1

    def update_ball_velocity(self):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.x) > (self.canvas_width - self.size):
            self.bounce_off_vertical_wall()

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.y) > (self.canvas_height - self.size):
            self.bounce_off_vertical_wall()

    def move(self, dt = 1 ):
        self.x += self.vx*dt
        self.y += self.vy*dt

    def draw_border(self):
        turtle.penup()
        turtle.goto(self.canvas_width * -1 , self.canvas_height * -1)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def __str__(self):
        return str(self.x) + ":" + str(self.y) + ":" + str(self.vx) + ":" + str(self.vy) + ":" + str(self.count) + str(self.id)

class Number : 
    def __init__(self,t):
        self.tom = t 
        self.tom_color = (255, 0, 0)

    def install(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        self.tom.color(self.tom_color)
        self.tom.penup()
        self.tom.setheading(0)
        self.tom.goto(0, 0)
        self.tom.pensize(10)

    def draw(self, digit):
        if digit == 0:
            self.tom.goto(-50, 100)
            self.tom.pendown()
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.penup()

        if digit == 1:
            self.tom.goto(50, 100)
            self.tom.pendown()
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.penup()

        if digit == 2:
            self.tom.goto(-50, 100)
            self.tom.pendown()
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.forward(100)
            self.tom.penup()

        if digit == 3:
            self.tom.goto(-50, 100)
            self.tom.pendown()
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.forward(-100)
            self.tom.left(90)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.left(90)
            self.tom.penup()

        if digit == 4:
            self.tom.goto(-50, 100)
            self.tom.pendown()
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.forward(100)
            self.tom.forward(-100)
            self.tom.forward(-100)
            self.tom.right(90)
            self.tom.penup()

        if digit == 5:
            self.tom.goto(-50, 100)
            self.tom.pendown()
            self.tom.forward(100)
            self.tom.forward(-100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.left(90)
            self.tom.penup()

        if digit == 6:
            self.tom.goto(-50, 100)
            self.tom.pendown()
            self.tom.forward(100)
            self.tom.forward(-100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.left(90)
            self.tom.penup()
            self.tom.goto(-50, 0)
            self.tom.pendown()
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.penup()
        
        if digit == 7:
            self.tom.goto(-50, 100)
            self.tom.pendown()
            self.tom.forward(100)
            self.tom.forward(-100)
            self.tom.goto(50, 100)
            self.tom.pendown()
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.penup()

        if digit == 8:
            self.tom.goto(-50, 100)
            self.tom.pendown()
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.penup()
            self.tom.goto(-50, 0)
            self.tom.pendown()
            self.tom.forward(100)
            self.tom.penup()

        if digit == 9:
            self.tom.goto(-50, 100)
            self.tom.pendown()
            self.tom.forward(100)
            self.tom.forward(-100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.left(90)
            self.tom.penup()
            self.tom.goto(50, 100)
            self.tom.pendown()
            self.tom.right(90)
            self.tom.forward(100)
            self.tom.left(90)
            self.tom.penup()

    def clear(self):
        self.tom.clear()

    @staticmethod
    def my_delay(dt = 0.2):
        start =  time.time()
        while time.time() - start < dt:
            pass

if __name__ == "__main__":
    canvas_width = turtle.screensize()[0]
    canvas_height = turtle.screensize()[1]
    print(canvas_width, canvas_height)
    ball_radius = 0.05 * canvas_width
    turtle.colormode(255)
    xpos = []
    ypos = []
    vx = []
    vy = []
    ball_color = []
    for i in range(0,5):
        xpos.append(random.uniform(-1*canvas_width + ball_radius, canvas_width - ball_radius))
        ypos.append(random.uniform(-1*canvas_height + ball_radius, canvas_height - ball_radius))
        vx.append(10*random.uniform(-1.0, 1.0))
        vy.append(10*random.uniform(-1.0, 1.0))
        ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    turtle.clear()
    
    
    tom = turtle.Turtle()
    num = Number(tom) 
    num.install()
    while True:
        for i in range(5):
            
            ball  = Ball(color = ball_color[i], size = ball_radius,x =  xpos[i], y = ypos[i], id = i , vx = vx[i] ,vy = vy[i] )
            ball.draw_border()
            ball.draw()
            ball.move()
            ball.update_ball_velocity()
            
            turtle.update()
        for i in range(0, 10):
            num.clear()
            num.draw(digit = i)
            num.my_delay()
            turtle.update()

turtle.done()
    