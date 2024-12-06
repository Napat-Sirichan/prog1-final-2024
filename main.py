import turtle
import math
import time



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
    tom = turtle.Turtle()
    num = Number(tom) 
    num.install()
    while True:
        for i in range(0, 10):
            num.clear()
            num.draw(digit = i)
            num.my_delay()
            turtle.update()
turtle.done()
    