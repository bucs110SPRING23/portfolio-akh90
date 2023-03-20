import turtle
import time

window = turtle.Screen()

turtle.Screen().bgcolor("white")

#building the house
color_walls = window.textinput("color_walls", "Let's build a house! Enter a color for the walls: ")

turtle.speed(5)
turtle.penup()
turtle.goto(-450,-200)
turtle.pendown()
turtle.title("House")

#Pen Details
turtle.pen(pencolor="green",pensize=2)

#floor
turtle.forward(900)
turtle.backward(250)
turtle.left(90)

#Walls
#color_walls = window.textinput("color_walls", "Let's build a house! Enter a color for the walls: ")
turtle.color(color_walls)
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(3)
turtle.right(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(5)
turtle.right(90)
turtle.forward(5)

turtle.left(90)
turtle.forward(150)
turtle.left(120)
turtle.forward(25)
turtle.right(120)
turtle.forward(20)
turtle.left(90)
turtle.forward(187)
turtle.end_fill()

turtle.right(90)
turtle.forward(175)

#Pillars
color_pillars1 = window.textinput("color_pillars", "Let's add some pillars! Enter a color for one of them: ")
turtle.speed(5)
turtle.color(color_pillars1)
turtle.begin_fill()
turtle.right(90)
turtle.forward(187)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(187)
turtle.end_fill()

color_pillars2 = window.textinput("color_pillars2", "Enter another color: ")
turtle.color(color_pillars2)
turtle.left(90)
turtle.forward(173)

color_pillars3 = window.textinput("color_pillars3", "Enter another color for the other pillar: ")
turtle.color(color_pillars3)
turtle.begin_fill()
turtle.left(90)
turtle.forward(187)
turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.forward(187)
turtle.end_fill()

turtle.backward(187)
turtle.right(90)
turtle.forward(2)
turtle.forward(180)

#Walls 2
turtle.speed(5)
turtle.color(color_walls)
turtle.begin_fill()
turtle.forward(192)
turtle.left(90)
turtle.forward(187)
turtle.left(90)
turtle.forward(193)
turtle.end_fill()
turtle.left(90)
turtle.forward(187)

#Pillars 2
turtle.speed(5)
turtle.color(color_pillars1)
turtle.begin_fill()
turtle.left(90)
turtle.forward(195)
turtle.left(90)
turtle.forward(187)
turtle.right(90)
turtle.forward(7)
turtle.right(90)
turtle.forward(187)
turtle.left(90)
turtle.forward(3)
turtle.right(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(3)
turtle.right(90)
turtle.forward(7)
turtle.right(90)
turtle.forward(188)
turtle.right(135)
turtle.forward(16)
turtle.end_fill()
turtle.right(225)

#Roof
color_roof = window.textinput("color_roof", "What color do you want the roof to be? ")
turtle.speed(5)
turtle.color(color_roof)
turtle.begin_fill()
turtle.right(-45)
turtle.forward(180)
turtle.right(94)
turtle.forward(170)
turtle.right(131)
turtle.forward(240)
turtle.end_fill()

#Roof 2
turtle.speed(5)
turtle.begin_fill()
turtle.right(-225)
turtle.forward(330)
turtle.right(94)
turtle.forward(285)
turtle.right(131)
turtle.forward(300)
turtle.end_fill()

#Roof 3
turtle.speed(5)
turtle.left(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(310)

turtle.begin_fill()
turtle.right(-225)
turtle.forward(130)
turtle.right(45)
turtle.forward(200)
turtle.right(-225)
turtle.forward(130)
turtle.end_fill()

#Trim
color_trim = window.textinput("color_trim", "What color would you like the roof trim to be? ")
turtle.speed(5)
turtle.color(color_trim)
turtle.right(45)
turtle.forward(200)
turtle.right(-225)
turtle.forward(130)
turtle.right(45)
turtle.forward(195)
turtle.right(-45)
turtle.forward(190)
turtle.right(94)
turtle.forward(287)
turtle.right(-229)
turtle.forward(195)
turtle.right(225)
turtle.forward(28)
turtle.right(-225)
turtle.forward(250)
turtle.right(135)
turtle.forward(180)
turtle.right(91)
turtle.forward(170)

turtle.right(134)
turtle.forward(240)

#Windows
turtle.speed(5)
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()
turtle.color("#91bfbe")
turtle.begin_fill()
turtle.forward(55)
turtle.right(90)
turtle.forward(130)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(130)
turtle.end_fill()

#Window Frame
color_windowframe = window.textinput("color_windowframe", "Enter a color for the window frames: ")
turtle.speed(10)
turtle.color(color_windowframe)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(130)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(130)

turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(65)
turtle.right(90)
turtle.forward(55)

turtle.right(90)
turtle.forward(65)
turtle.right(90)
turtle.forward(27.5)
turtle.right(90)
turtle.forward(130)

#Door
color_door = window.textinput("color_door", "What color would you like the door to be? ")
turtle.color(color_door)
turtle.penup()
turtle.left(90)
turtle.forward(115)
turtle.left(90)
turtle.forward(225)
turtle.pendown()

turtle.begin_fill()
turtle.left(90)
turtle.forward(135)
turtle.right(90)
turtle.forward(65)
turtle.right(90)
turtle.forward(135)
turtle.end_fill()

#Window 2
turtle.penup()
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(100)
turtle.pendown()

turtle.color("#91bfbe")
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(95)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(95)
turtle.end_fill()

#Window Frame
turtle.color(color_windowframe)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(95)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(95)

turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(95)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(47.5)
turtle.right(90)
turtle.forward(50)

time.sleep(3)
turtle.hideturtle()
turtle.clear()
turtle.Screen().bgcolor("dark sea green")

numb_petals = int(window.textinput("numb_petals", "Let's make you a flower to decorate your house with! Enter the number of petals you want: "))
color_petals = window.textinput("color_petals", "Enter the color of petals you want: ")


def draw_petal(t, radius, angle):
    #Draws a single petal using the turtle t
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)

def draw_flower(t, numb_petals, radius, angle):
    #Draws the flower with numb_petals using t turtle
    for _ in range(numb_petals):
        draw_petal(t, radius, angle)
        t.left(360 / numb_petals)

def main():
#Draws a flower using the turtle library
    # Create the turtle and set some initial settings
    t = turtle.Turtle()
    t.speed(5)  # Set the turtle speed to maximum

    # Draw the petals of the flower
    t.color( 'black', color_petals,)
    t.begin_fill()
    draw_flower(t, numb_petals, radius=200, angle=60)
    t.end_fill()

   

    # Hide the turtle
    t.hideturtle()

    # Exit on click
    turtle.exitonclick()

if __name__ == '__main__':
    main()

