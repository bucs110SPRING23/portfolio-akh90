import turtle

sides = input("enter a number of sides: ")
sides = int (sides)

length = int(input("enter a length of the sides: "))

pen = turtle.Turtle()
pen.color ("orange")

window = turtle.Screen()

for s in range (sides):
    pen.forward(length)
    pen.right(360 / sides)

#for s in range (sides):
 #   print(s)

window.exitonclick()