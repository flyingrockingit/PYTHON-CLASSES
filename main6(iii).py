import turtle
turtle.Screen().bgcolor('White')
sc=turtle.Screen()
sc.setup(500,400)
turtle.title("Welcome to the world of Spiral Rainbow!")
pen=turtle.Turtle()
colors=['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
pen.hideturtle()
while True:
    for x in range (200):
        pen.pencolor(colors[x%len(colors)])
        pen.width(x/100+1)
        pen.forward(x)
        pen.left(59)
    for x in range (200,0,-1):
        pen.pencolor("White")
        pen.width(x/100+7)
        pen.forward(x)
        pen.left(59)
turtle.done()