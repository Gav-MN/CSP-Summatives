import turtle as trtl
import random as rand
import os
import sys

#---------Screen Setup---------------
easy = [1,2,3,4]
normal = [3,4,5,6]
hard = [0,7,10,999]
turtle_colors = ["red", "red", "red"]
turtle_shapes = ["square", "square", "square"]
cups = []
hori = -150
font_setup = ("Arial", 20, "normal")
loop = 1
e =  trtl.Turtle()
n =  trtl.Turtle()
h =  trtl.Turtle()
difficulty_chosen = False
wn = trtl.Screen()
#---------Shape creation---------------
ball = trtl.Turtle("circle")
ball.color("black", "blue")
ball.penup()
ball.shapesize(2)

for s in turtle_shapes:
  cup = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  cup.color("black", new_color)
  cup.penup()
  cup.speed(0)
  cups.append(cup)
  cup.goto(hori, 100)
  hori = hori + 150
  cup.shapesize(5)
#---------Question creation---------------
e.penup()
e.hideturtle()
e.goto(-90, 300)
e.write("Activate Easy Mode", font=font_setup)
n.penup()
n.hideturtle()
n.goto(-90, 250)
n.write("Activate Normal Mode", font=font_setup)
h.penup()
h.hideturtle()
h.goto(-90, 200)
h.write("Activate Hard Mode", font=font_setup)
#-----game functions-------
def on_click(x, y):
    global difficulty_chosen
    if difficulty_chosen:
        return
    if -90 <= x <= 90 and 300 <= y <= 320:
        difficulty_chosen = "Easy"
        e.undo(); n.undo(); h.undo()
        h.write("Easy Mode Activated", font=font_setup)
    elif -90 <= x <= 90 and 250 <= y <= 270:
        difficulty_chosen = "Normal"
        e.undo(); n.undo(); h.undo()
        h.write("Normal Mode Activated", font=font_setup)
    elif -90 <= x <= 90 and 200 <= y <= 220:
        difficulty_chosen = "Hard"
        e.undo(); n.undo(); h.undo()
        h.write("Hard Mode Activated", font=font_setup)
    start_game(difficulty_chosen)

wn.onclick(on_click)

def start_game(mode):
    setup()
    game()

def setup():
  global pos0, pos1, pos2
  cups[0].speed(1)
  cups[1].speed(1)
  cups[2].speed(1)
  cups[0].goto(-150, 0)
  cups[1].goto(0, 0)
  cups[2].goto(150, 0)
  pos0 = cups[0].pos()
  pos1 = cups[1].pos()
  pos2 = cups[2].pos()

def show_play_again():
    e.write("Want To Play Again?", font=font_setup)
    n.write("Want To End?", font=font_setup)

    wn.onclick(play_again)

def play_again(x, y):
    if -90 <= x <= 90 and 300 <= y <= 320:
        os.execv(sys.executable, ['python'] + sys.argv)
    elif -90 <= x <= 90 and 250 <= y <= 270:
        exit()

def swap():
   global a, b
   cor1 = a.pos()
   cor2 = b.pos()
   a.goto(cor2)
   b.goto(cor1)

def game():
  global pos0, pos1, pos2, a, b
  if difficulty_chosen == "Easy":
    ball.hideturtle()
    for _ in range(10):
        cups[0].speed(rand.choice(easy))
        cups[1].speed(rand.choice(easy))
        cups[2].speed(rand.choice(easy))
        a, b = rand.sample(cups, 2)
        swap()
  elif difficulty_chosen == "Normal":
    ball.hideturtle()
    for _ in range(10):
        cups[0].speed(rand.choice(normal))
        cups[1].speed(rand.choice(normal))
        cups[2].speed(rand.choice(normal))
        a, b = rand.sample(cups, 2)
        swap()
  elif difficulty_chosen == "Hard":
    ball.hideturtle()
    for _ in range(20):
        cups[0].speed(rand.choice(hard))
        cups[1].speed(rand.choice(hard))
        cups[2].speed(rand.choice(hard))
        a, b = rand.sample(cups, 2)
        swap()
  show_play_again()


wn.mainloop()

