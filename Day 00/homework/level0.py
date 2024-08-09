from turtle import *


# Set pen speed
speed(30)

width(3)


# main shape
color("purple")
forward(260)
left(90)
forward(200)
left(90)
# color("red")
forward(260)
# color("purple")
left(90)
forward(200)


# door starting point
penup()
left(90)
forward(90)
pendown()

# door
color("yellow")
left(90)
forward(120)
right(90)
forward(80)
right(90)
forward(120)
color("black")

# roof starting point
penup()
left(90)
forward(90)
left(90)
forward(200)
pendown()

# roof
color("red")
begin_fill()
left(45)
forward(184)
left(90)
forward(184)
end_fill()
color("black")

# windows
penup()
left(45)
forward(60)
pendown()

# left window start position
left(90)
penup()
forward(20)
pendown()

# left window
forward(50)
right(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)

# right window starting position
penup()
right(90)
forward(170)
pendown()

# right window
forward(50)
right(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)





exitonclick()