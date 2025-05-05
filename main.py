import turtle

screen =turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("light pink")
t=turtle.Turtle()
t2=turtle.Turtle()

#intro screen
t.penup()
t.goto(0,100)
t.pendown()
t.write("Turtle presentation",font=("arial",30,"bold"),align="center")
t.penup()
t.goto(-275,0)
t.pendown()
t.fillcolor("purple")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()
t.penup()
t.goto(0,-100)
t.pendown()
t.write("By Evalyse Polito",font=("arial",30,"italic"),align="center")

t2.penup()
t2.goto(0,250)
t2.pendown()
t2.write("Press Enter to Continue",font=("arial",10,"bold"),align="center")

round = input("Press Enter to Continue")
t.clear()
t2.clear()
#second screen
t.penup()
t.goto(0,100)
t.pendown()
t.write("Favorite Foods",font=("arial",30,"bold"),align="center")
t.penup()
t.penup()
t.goto(-275,0)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.forward(50)
t.left(100)
t.forward(50)
t.left(100)
t.forward(50)
t.left(100)
t.forward(50)
t.left(100)
t.end_fill()
t.penup()
#pic1
t.goto(-120,-175)
t.pendown()
screen.addshape("download.gif")
t.shape("download.gif")
t.stamp()
t.shape("classic")
t.penup()
t.goto(-120,-275)
t.pendown()
t.write("Steak and Potatoes",font=("arial",10,"bold"),align="center")




#pic2
t.penup()
t.goto(0,0)
t.pendown()
screen.addshape("image.gif")
t.shape("image.gif")
t.stamp()
t.shape("classic")
t.penup()
t.goto(0,-100)
t.pendown()
t.write("Cheese Cake",font=("arial",10,"bold"),align="center")


#pic3
t.penup()
t.goto(120,-175)
t.pendown()
screen.addshape("pasta.gif")
t.shape("pasta.gif")
t.stamp()
t.shape("classic")
t.penup()
t.goto(120,-275)
t.pendown()
t.write("Pasta",font=("arial",10,"bold"),align="center")

t2.penup()
t2.goto(0,250)
t2.pendown()
t2.write("Press Enter to Continue",font=("arial",10,"bold"),align="center")


round = input("Press Enter to Continue")
t.clear()
t2.clear()
#screen2
t.penup()
t.goto(0,100)
t.pendown()
t.write("Hobbies",font=("arial",30,"bold"),align="center")
t.penup()
t.penup()
t.goto(-275,0)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()
t.penup()
#screen2 pic1
t.goto(-120,-175)
t.pendown()
screen.addshape("cheer1.gif")
t.shape("cheer1.gif")
t.stamp()
t.shape("classic")
t.penup()
t.goto(-120,-275)
t.pendown()
t.write("Cheerleading",font=("arial",10,"bold"),align="center")

t.penup()
t.goto(-120,0)
t.pendown()
screen.addshape("tanning.gif")
t.shape("tanning.gif")
t.stamp()
t.shape("classic")
t.penup()
t.goto(-120,-75)
t.pendown()
t.write("Tanning",font=("arial",10,"bold"),align="center")


t.penup()
t.goto(120,0)
t.pendown()
screen.addshape("sleeping.gif")
t.shape("sleeping.gif")
t.stamp()
t.shape("classic")
t.penup()
t.goto(120,-75)
t.pendown()
t.write("Sleeping",font=("arial",10,"bold"),align="center")


t.penup()
t.goto(120,-175)
t.pendown()
screen.addshape("shopping.gif")
t.shape("shopping.gif")
t.stamp()
t.shape("classic")
t.penup()
t.goto(120,-275)
t.pendown()
t.write("Shopping",font=("arial",10,"bold"),align="center")

t2.penup()
t2.goto(0,250)
t2.pendown()
t2.write("Press Enter to Continue",font=("arial",10,"bold"),align="center")

round = input("Press Enter to Continue")
t.clear()
t2.clear()
#screen3
t.penup()
t.goto(0,100)
t.pendown()
t.write("Favorite Movie",font=("arial",30,"bold"),align="center")
t.penup()
t.penup()
t.goto(-265,0)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()


#screen3pic1
t.penup()
t.goto(0,-175)
t.pendown()
screen.addshape("movie.gif")
t.shape("movie.gif")
t.stamp()
t.shape("classic")
t.penup()
t.goto(0,175)
t.pendown()
t.write("Ten things I hate about you",font=("arial",10,"bold"),align="center")

t2.penup()
t2.goto(0,250)
t2.pendown()
t2.write("Press Enter to Continue",font=("arial",10,"bold"),align="center")





round = input("Press Enter to Continue")
t.clear()
t2.clear()
#screen4
t.penup()
t.goto(0,100)
t.pendown()
t.write("Favorite Sport",font=("arial",30,"bold"),align="center")
t.penup()
t.goto(275,0)
t.pendown()
t.begin_fill()
t.fillcolor("hot pink")
t.circle(75)
t.end_fill()
#screen4pic1
t.penup()
t.goto(0,-175)
t.pendown()
screen.addshape("cheer.gif")
t.shape("cheer.gif")
t.stamp()
t.shape("classic")
t.penup()
t.goto(0,175)
t.pendown()
t.write("Cheerleading",font=("arial",30,"bold"),align="center")

t.clear()















turtle.done()