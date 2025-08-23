import turtle
turtle.Screen().bgcolor('Orange')
sc=turtle.Screen()
sc.setup(500,400)
turtle.title("Welcome to the world of Turtle!")
pen=turtle.Turtle()
for i in range (6):
    pen.forward(100)
    pen.left(60)
    i+=1
turtle.done()