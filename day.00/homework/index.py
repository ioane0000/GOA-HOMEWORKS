from turtle import *

#we want to paint a house

#step 1:  draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of sqware

#drawing a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red") 
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing window

left(30)
color("purple")

forward(70)
left(90)
forward(7)
left(90)
color("white")
forward(50)
right(180)
forward(55)
left(90)
forward(10)
left(90)
color("blue")
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
forward(7)
right(90)
color("white")
forward(60)
right(180)
forward(70)
right(180)
forward(70)
right(90)
forward(170)
right(90)
color("blue")
forward(60)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(57)
right(90)
color("white")
forward(20)
right(180)
forward(27)
left(90)
forward(50)
right(90)
forward(7)
right(90)
forward(55)



exitonclick()