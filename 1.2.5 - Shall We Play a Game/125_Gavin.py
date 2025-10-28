import turtle as trtl
import random as rand

#---------Screen Setup---------------
turtle_colors = ["red", "red", "red"]
turtle_shapes = ["square", "square", "square"]
cups = []
hori = -150

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
  cups.append(cup)
  cup.goto(hori, 100)
  hori = hori + 150
  cup.shapesize(5)

spot0 = cups[0]
spot1 = cups[1]
spot2 = cups[2]










wn = trtl.Screen()
wn.mainloop()
 