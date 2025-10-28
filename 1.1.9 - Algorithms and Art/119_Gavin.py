import turtle as trtl
import random

wn = trtl.Screen()
wn.setup(width=1000, height=1000)
screen_width = 500
screen_height = 300
x_min = -screen_width
x_max = screen_width
y_min = -screen_height
y_max = screen_height

meme = ["star", "7", "6"]
shape = ["star", "blank", "arrow", "circle", "turtle", "square", "triangle", "classic"]
color = ["red","red1","red2","red3","red4","DarkRed","IndianRed","IndianRed1","IndianRed2","IndianRed3","IndianRed4","orange","orange1","orange2","orange3","orange4","DarkOrange","DarkOrange1","DarkOrange2","DarkOrange3","DarkOrange4","OrangeRed","OrangeRed1","OrangeRed2","OrangeRed3","OrangeRed4","yellow","yellow1","yellow2","yellow3","yellow4","LightYellow","LightYellow1","LightYellow2","LightYellow3","LightYellow4","LemonChiffon","LemonChiffon1","LemonChiffon2","LemonChiffon3","LemonChiffon4","LightGoldenrod","LightGoldenrod1","LightGoldenrod2","LightGoldenrod3","LightGoldenrod4","gold","gold1","gold2","gold3","gold4","goldenrod","goldenrod1","goldenrod2","goldenrod3","goldenrod4","PaleGoldenrod","green","green1","green2","green3","green4","DarkGreen","DarkOliveGreen","DarkOliveGreen1","DarkOliveGreen2","DarkOliveGreen3","DarkOliveGreen4","DarkSeaGreen","DarkSeaGreen1","DarkSeaGreen2","DarkSeaGreen3","DarkSeaGreen4","LightGreen","PaleGreen","PaleGreen1","PaleGreen2","PaleGreen3","PaleGreen4","SpringGreen","SpringGreen1","SpringGreen2","SpringGreen3","SpringGreen4","LawnGreen","lawngreen","SeaGreen","SeaGreen1","SeaGreen2","SeaGreen3","SeaGreen4","ForestGreen","blue","blue1","blue2","blue3","blue4","DarkBlue","LightBlue","LightBlue1","LightBlue2","LightBlue3","LightBlue4","DeepSkyBlue","DeepSkyBlue2","DeepSkyBlue3","DeepSkyBlue4","DodgerBlue","DodgerBlue1","DodgerBlue2","DodgerBlue3","DodgerBlue4","CornflowerBlue","RoyalBlue","RoyalBlue1","RoyalBlue2","RoyalBlue3","RoyalBlue4","SteelBlue","SteelBlue1","SteelBlue2","SteelBlue3","SteelBlue4","LightSteelBlue","LightSteelBlue1","LightSteelBlue2","LightSteelBlue3","LightSteelBlue4","LightSkyBlue","LightSkyBlue1","LightSkyBlue2","LightSkyBlue3","LightSkyBlue4","SkyBlue","SkyBlue1","SkyBlue2","SkyBlue3","SkyBlue4","MidnightBlue","midnightblue","Navy","navy","Azure","azure","azure1","azure2","azure3","azure4","purple","purple1","purple2","purple3","purple4","MediumPurple","MediumPurple1","MediumPurple2","MediumPurple3","MediumPurple4","silver"]

trtl.addshape("star", ((0,10),(-3,2),(-11,2),(-4,-3),(-7,-11),(0,-6),(7,-11),(4,-3),(11,2),(3,2)))
trtl.addshape("7", ((1, 10),(9, 10),(9,8),(6, -1),(4, -1),(7, 8),(0.5, 8)))
trtl.addshape("6", ((0, 7),(0, 8),(-1, 10),(-6, 10),(-7, 8),(-7, 1),(-6, -1),(-1,-1),(0, 1),(0, 3),(-1, 5),(-5, 5),(-5, 3.5),(-2, 3.5),(-2, 0.5),(-5, 0.5),(-5, 8.5),(-2,8.5),(-2,7)))

screen = trtl.Screen()
screen.title("User Input Example")
number = trtl.textinput("Number Input", "Pick a number 1-100")
satisfaction="n"

while satisfaction == "n":
    trtl.penup()
    if (number=="67"):
        trtl.shapesize(10)
        trtl.color("gold")
        trtl.left(90)
        trtl.shape("star")
        trtl.stamp()
        trtl.color("silver")
        trtl.shapesize(5)
        trtl.backward(40)
        trtl.pendown
        trtl.shape("6")
        trtl.stamp()
        trtl.shape("7")
        trtl.stamp()
        trtl.shapesize(2)
        for s in shape:
            trtl.shape(random.choice(meme))
            trtl.color(random.choice(color))
            random_x = random.randint(int(x_min), int(x_max))
            random_y = random.randint(int(y_min), int(y_max))
            trtl.goto(random_x, random_y)
            trtl.stamp()

    else:
        trtl.shapesize(2)
        for s in shape:
            trtl.shape(random.choice(shape))
            trtl.color(random.choice(color))
            random_x = random.randint(int(x_min), int(x_max))
            random_y = random.randint(int(y_min), int(y_max))
            trtl.goto(random_x, random_y)
            trtl.stamp()

    satisfaction = trtl.textinput("Satisfaction Input", "Are you entertained (y/n)")



wn = trtl.Screen()
wn.mainloop()
