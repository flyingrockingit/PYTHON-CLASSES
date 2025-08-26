import turtle

sc = turtle.Screen()
sc.bgcolor("black")
sc.setup(800, 600)
turtle.title("Pastel Spiral Flower")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

pen.penup()
pen.goto(0, 100)
pen.pendown()

colors = [
    "#FFB6C1",  
    "#FFDAB9",  
    "#FFFACD",  
    "#E0FFFF", 
    "#D8BFD8",  
    "#B0E0E6"   
]

for i in range(75):
    pen.color(colors[i % 6])   
    pen.circle(100)
    pen.left(5)

turtle.done()
