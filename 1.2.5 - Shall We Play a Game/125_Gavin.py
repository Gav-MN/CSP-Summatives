import turtle as trtl
import random as rand
import os
import sys

#---------Screen Setup---------------
easy = [1,2,3,4]
normal = [1,2,3,4,5,6,8,9,10]
hard = [0,7,10,999]
turtle_colors = ["red", "red", "red"]
turtle_shapes = ["square", "square", "square"]
cups = []
hori = -150
font_setup = ("Arial", 20, "normal")
loop = 1
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

pos0 = cups[0].pos()
pos1 = cups[1].pos()
pos2 = cups[2].pos()

difficulty = trtl.textinput("Difficulty", "Choose your difficulty (1, 2, 3)")
trtl.penup()
trtl.hideturtle()
trtl.goto(-90, 200)

if difficulty == "1":
  trtl.write("Easy mode activated", font=font_setup)
  cups[0].speed(rand.choice(easy))
  cups[1].speed(rand.choice(easy))
  cups[2].speed(rand.choice(easy))
  cups[0].goto(-150, 0)
  cups[1].goto(0, 0)
  cups[2].goto(150, 0)
  while 1==1:
    if loop == 11:
      break
    else:
      loop += 1
      cups[0].speed(rand.choice(easy))
      cups[1].speed(rand.choice(easy))
      cups[2].speed(rand.choice(easy))
      rand.choice()
elif difficulty == "2":
  trtl.write("Normal mode activated", font=font_setup)
  cups[0].speed(rand.choice(normal))
  cups[1].speed(rand.choice(normal))
  cups[2].speed(rand.choice(normal))
  cups[0].goto(-150, 0)
  cups[1].goto(0, 0)
  cups[2].goto(150, 0)
  while 1==1:
    if loop == 11:
      break
    else:
      loop += 1
      cups[0].speed(rand.choice(normal))
      cups[1].speed(rand.choice(normal))
      cups[2].speed(rand.choice(normal))
elif difficulty == "3":
  trtl.write("Hard mode activated", font=font_setup)
  cups[0].speed(rand.choice(hard))
  cups[1].speed(rand.choice(hard))
  cups[2].speed(rand.choice(hard))
  cups[0].goto(-150, 0)
  cups[1].goto(0, 0)
  cups[2].goto(150, 0)
  while 1==1:
    if loop == 11:
      break
    else:
      loop += 1
      cups[0].speed(rand.choice(hard))
      cups[1].speed(rand.choice(hard))
      cups[2].speed(rand.choice(hard))


pa = trtl.textinput("Play Again", "Would you like to play again? (y/n)")

if pa == "y":
  os.execv(sys.executable, ['python'] + sys.argv)
else:
  exit()

wn = trtl.Screen()
wn.mainloop()
 