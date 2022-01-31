import random
import turtle
wn = turtle.Screen()

##Abstract
def setUpScreen():
    turtle.setup(1024, 768)
    turtle.colormode(255)
    r1 = 10
    b1 = 10
    g1 = 10
    for i in range(400):
        r1 += random.randrange(2)
        b1 += random.randrange(2)
        g1 += random.randrange(2)
        wn.bgcolor([r1,b1,g1])

def drawBox():
    trashturtle = turtle.Turtle()
    trashturtle.penup()
    trashturtle.speed(0)
    trashturtle.backward(300)
    trashturtle.left(90)
    trashturtle.forward(300)
    trashturtle.pendown()
    wn.update()
    for i in range(4):
        trashturtle.backward(600)
        trashturtle.left(90)
    trashturtle.ht()
def calculate(massOneInput, massTwoInput, velOneInput, velTwoInput):
    totalMassVel = (massOneInput * velOneInput) + (massTwoInput * velTwoInput)
    totalVel = totalMassVel / (massOneInput + massTwoInput)
    return totalVel


 

##Algorithm
def setUp():
    drawBox()
    print("This will be a perfectly inelastic collision simulation (The objects will collide and stick together)")
    mass1 = int(input("How big is the mass of the first object?"))
    vel1 = int(input("How fast is the first object moving? (positive number, less than or equal to 30, and multiple of 10's only)"))
    mass2 = int(input("How big is the mass of the second object?"))
    vel2 = int(input("How fast is the second object moving? (negative number, more than or equal to -30, and multiple of 10's only)"))
    massO = turtle.Turtle()
    massO.penup()
    massO.shape("circle")
    massO.color("black")
    massO.shapesize(1)
    massT = turtle.Turtle()
    massT.penup()
    massT.shape("circle")
    massT.color("white")
    massT.shapesize(1)
    massO.backward(150)
    massT.forward(150)
    massT.left(180)
    while(massO.xcor() != 0):
        massO.forward(vel1/10)
    while(massT.xcor() != 0):
        massT.forward(abs(vel2/10))
    if (calculate(mass1, mass2, vel1, vel2) > 0 or calculate(mass1, mass2, vel1, vel2) < 0):
        turtle3 = turtle.Turtle()
        massO.ht()
        massT.ht()
        turtle3.shape("circle")
        turtle.color("gray")
        turtle3.goto(0,0)
        while(turtle3.xcor() > -300 and turtle3.xcor() < 300):
            turtle3.forward(calculate(mass1, mass2, vel1, vel2))
    print("The speed of the two objects when they collide and stick will be " + str(calculate(mass1, mass2, vel1, vel2)) + " meters per second.")
        
setUpScreen()
setUp()
