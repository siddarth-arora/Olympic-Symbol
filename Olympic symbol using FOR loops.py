import turtle
wn = turtle.Screen()
bob = turtle.Turtle()
color = ("blue","black","red")
colors = ("yellow","green")
bob.setposition(0, 0)
m = 0

for c in color:         #CREATES THE FIRST ROW OF CIRCLES WHICH INCLUDE BLUE, BLACK AND RED CIRCLES 
	bob.penup()
	bob.fd(m)
	m = 75
	bob.pendown()
	bob.color(c)
	bob.circle(50)

bob.penup()
bob.setposition(37.5, -75)
bob.pendown()
m = 0

for c in colors:        #CREATES THE SECOND ROW OF CIRCLES WHICH INCLUDE YELLOW AND GREEN CIRCLES 
	bob.penup()
	bob.fd(m)
	m = 75
	bob.pendown()
	bob.color(c)
	bob.circle(50)


wn.exitonclick()

