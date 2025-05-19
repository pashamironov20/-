from turtle import *
import turtle

screen = turtle.Screen()
screen.title("симулятор летчика")

screen.bgcolor("lightblue")

player = Turtle()
player.color("white")
player.penup()
player.shape("triangle")

def forward():
 player.forward(100)
 
def back():
 player.backward(100)

def left():
 player.left(90)
 
def right():
 player.right(90)
 
screen.listen()

screen.onkey(forward, 'Right')
screen.onkey(back, 'Left')
screen.onkey(left, 'Up')
screen.onkey(right, 'Down')

screen.mainloop()
