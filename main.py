import turtle

screen =turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("light pink")
t=turtle.Turtle()

#intro screen
t.penup()
t.goto(0,100)
t.pendown()
t.write("Turtle presentation",font=("arial",30,"bold"),align="center")
t.penup()
t.goto(0,-100)
t.pendown()
t.write("By Evalyse Polito",font=("arial",30,"italic"),align="center")

round = input("Press Enter to Continue")
t.clear()

#second screen
t.penup()
t.goto(0,100)
t.pendown()
t.write("Favorite Foods",font=("arial",30,"bold"),align="center")
t.penup()

#pic1
t.goto(-120,-175)
t.pendown()
screen.addshape("download.gif")
t.shape("download.gif")
t.stamp()
t.shape("classic")

#pic2
t.penup()
t.goto(0,0)
t.pendown()
screen.addshape("image.gif")
t.shape("image.gif")
t.stamp()
t.shape("classic")

#pic3
t.penup()
t.goto(120,-175)
t.pendown()
screen.addshape("pasta.gif")
t.shape("pasta.gif")
t.stamp()
t.shape("classic")




































turtle.done()