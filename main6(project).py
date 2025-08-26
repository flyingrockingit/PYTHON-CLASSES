import turtle

sc = turtle.Screen()
sc.bgcolor('White')
sc.setup(800, 600)  
turtle.title("Welcome to the world of Turtle Library Shapes!")

pen = turtle.Turtle()
pen.pensize(10)

for i in range(3):
    pen.forward(100)
    pen.left(120)

pen.penup()
pen.goto(200, 0)   
pen.pendown()
for i in range(4):
    pen.forward(100)
    pen.left(90)

pen.penup()
pen.goto(-200, 0)   
pen.pendown()
for i in range(5):
    pen.forward(100)
    pen.right(144)

pen.penup()
pen.goto(0, -200)   
pen.pendown()
for i in range(6):
    pen.forward(100)
    pen.left(60)

pen.penup()
pen.goto(-400, 0)   
pen.pendown()
pen.color("red", "pink")
pen.begin_fill()

pen.setheading(0)   
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)

pen.end_fill()

turtle.done()
