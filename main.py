import turtle
from turtle import Screen
my_screen = Screen()
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("white")
t.pencolor("black")
t.width(10)
def up():
    t.forward(50)
def left():
    t.left(90)
def right():
    t.right(90)
turtle.onkeypress(up,"Up")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()

colors=["red", "orange", "yellow", "green", "blue", "purple", "gray", "brown", "aqua", "sea green"]
your_name = turtle.textinput("Enter Your Name", "What Is Your Name?")
sides = int(turtle.numinput("Number Of Sides", "How Many Sides Do You Want (1-10)", 5, 1, 10))
for x in range(100):
    t.pencolor(colors[x%sides%10])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font=("Times", int( (x*2 + 4) /4), "bold"))
    t.left(360/sides+2)

my_screen.exitonclick()