from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()


def move_forwards():
    tim.forward(18)
def move_backwards():
    tim.backward(18)
def turn_left():
    new_heading = tim.heading() + 18
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 18
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

my_screen.listen()
my_screen.onkey(move_forwards, "w")
my_screen.onkey(move_backwards, "s")
my_screen.onkey(turn_left, "a")
my_screen.onkey(turn_right, "d")
my_screen.onkey(clear, "c")

my_screen.exitonclick()