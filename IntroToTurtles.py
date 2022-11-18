#turtles intro
import turtle

t = turtle.Pen()
s = turtle.Screen()
s.bgcolor("white")

s.title("Intro To Turtles!!") #creates a fun little title at top of the window

for x in range(4): #runs the following commands the number of times specified in the range function
    t.pendown()#puts the pen down.  If your turtle isn't drawing, make sure you have this command written.
    t.pencolor("black")
    t.fd(100)
    t.rt(90)

t.penup()#takes the pen up

s.exitonclick()