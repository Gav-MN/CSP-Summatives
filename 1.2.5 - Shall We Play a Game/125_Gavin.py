import turtle as trtl
import random as rand

#---------Screen Setup---------------
turtle_colors = ["red", "red", "red"]
turtle_shapes = ["square", "square", "square"]
cups = []
hori = -150
font_setup = ("Arial", 20, "normal")

#---------Shape creation---------------
ball = trtl.Turtle("circle")
ball.color("blue")
ball.penup()
ball.shapesize(2)

for s in turtle_shapes:
  cup = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  cup.color(new_color)
  cup.penup()
  cup.speed(0)
  cups.append(cup)
  cup.goto(hori, 100)
  hori = hori + 150
  cup.shapesize(5)

cor0 = cups[0]
cor1 = cups[1]
cor2 = cups[2]
ballcor = ball

difficulty = trtl.textinput("Difficulty", "Choose your difficulty (1, 2, 3)")

if difficulty == "1":
  trtl.penup()
  trtl.hideturtle()
  trtl.goto(-90, 200)
  trtl.write("Easy mode activated", font=font_setup)






wn = trtl.Screen()
wn.mainloop()
 