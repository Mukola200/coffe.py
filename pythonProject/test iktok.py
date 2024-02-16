from turtle import*

title('R')

bgcolor('light green')
pencolor('red')
pensize(15)

setheading(90)

forward(280)
right(90)
forward(50)
circle(-60,180)
forward(50)

left(180)
forward(25)
right(60)
forward(190)
hideturtle()
clear()

title('black')

shape('square')
pensize(7)
pencolor('red')

begin_fill()
fillcolor('yellow')

for i in range(5):
    forward(250)
    left(144)

clear()
hideturtle()

from turtle import*

bgcolor('light blue')

pencolor('grey')
pensize(5)
begin_fill()
fillcolor('orange')

for i in range(3):
    forward(150)
    left(120)
    dot(25)
end_fill()
hideturtle()