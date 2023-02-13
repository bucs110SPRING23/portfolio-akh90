import turtle
import math
# simulates pen and paper, can be used to draw
pen = turtle.Turtle() 
pen2 = turtle.Turtle()   #function = will always have ()
pen.shape("turtle")
pen2.shape("turtle")
pen.color ("purple")
pen2.color ("orange")
pen.speed (1)
pen.speed (1) #speed is 1-10 with 1 the slowest. 0 is the fastest after 10



window = turtle.Screen()
# variable = module.funtion()

pen. forward (100) # fd does the same thing as forward
pen. left (90) 
pen. forward (100) 
pen. left (90) 
pen. forward (100) 
pen. left (90)
pen. forward (100) 
pen. left (90)



pen2.fd (50)
pen2.left (5)
pen2.up() #picks the pen up
pen2.fd (50)
pen2.left (5)
pen2.down()
pen2.fd (50)
pen2.left (5)
pen2.up()


pen2.home () #goes to the origin same as xx.goto(0,0)
pen.goto(13,67)

#var = math.pi

# interface: what can i tell it to do? abstract away the details
# state: value of all its attributes
var = [1, 2, 3, 4, 5]
var.append(6) #add to the end



window.exitonclick()  #always must be the last turtle command


