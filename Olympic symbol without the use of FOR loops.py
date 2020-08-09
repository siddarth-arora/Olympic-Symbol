import turtle

wn = turtle.Screen()
bob = turtle.Turtle()
bob.pensize(8)



bob.penup()              #CREATES A BLUE CIRCLE AT THE APPROPRIATE POSITION
bob.setposition(25,50)
bob.color("blue")
bob.pendown()
bob.circle(50)

bob.penup()               #CREATES A BLACK CIRCLE AT THE APPROPRIATE POSITION
bob.setposition(75,50)
bob.color("black")
bob.pendown()
bob.circle(50)

bob.penup()                 #CREATES A RED CIRCLE AT THE APPROPRIATE POSITION
bob.setposition(125,50)
bob.color("red")
bob.pendown()
bob.circle(50)

bob.penup()                #CREATES A YELLOW CIRCLE AT THE APPROPRIATE POSITION
bob.setposition(50,-25)
bob.color("yellow")
bob.pendown()
bob.circle(50)

bob.penup()                #CREATES A GREEN CIRCLE AT THE APPROPRIATE POSITION
bob.setposition(100,-25)
bob.color("green")
bob.pendown()
bob.circle(50)


wn.exitonclick()















'''import turtle 
bob = turtle.Turtle()
wn = turtle.Screen()
colours = ("blue","yellow","black","green","red")
angle = (45,225,45,225,0)
n = 0
bob.setposition(0,0)
for c in colours:
	bob.color(c)
	bob.penup()
	bob.rt(angle[n])
	n =+ 1
	bob.fd(50)
	bob.pendown()
	bob.circle(50)

wn.exitonclick()
'''














