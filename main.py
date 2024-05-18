from turtle import Turtle, Screen
import ctypes


fields = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")
coordinates = [(-300, -300), (-300, -100), (-300, 100), (-100, -300), (-100, -100), (-100, 100), (100, -300), (100, -100), (100, 100)]
# field gives an array with each a tuple with the: 'name', x_pos, y_pos for creating all the 9 field spots
# middle of the screen has the coordinate point (0,0)
turtles = []

SIZE = 600
RADIUS = SIZE/6
player = 1          # player 1 is: X; player 2 is: O

screen = Screen()
screen.setup(SIZE, SIZE)
screen.title(" | --- TicTacToe --- |")


class MyTurtle(Turtle):
    def __init__(self, name, x_pos, y_pos):
        Turtle.__init__(self)
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed(0)
        self.shape("square")
        self.shapesize(5, 5, 100)
        self.color("white")
        self.pu()
        self.goto((x_pos+100), (y_pos+100))

    def set_O_Shape(self):
        # reset turtle
        self.reset()
        self.speed(0)
        # start poly
        self.begin_poly()
        self.circle(RADIUS-20)
        self.end_poly()
        poly = self.get_poly()
        screen.register_shape("O", poly)
        self.shape("O")
        # orientation
        self.clear()
        self.pu()

    def set_X_Shape(self):
        # reset turtle
        self.reset()
        self.speed(0)
        # start poly
        self.begin_poly()
        for i in range(4):
            self.fd(RADIUS)
            self.back(RADIUS)
            self.lt(90)
        self.end_poly()
        poly = self.get_poly()
        screen.register_shape("X", poly)
        self.shape("X")
        # orientation
        self.clear()
        self.pu()
        self.rt(45)
        self.shapesize(1,1,20)

    def set_X(self):
        # exchange the empty field to a 'X' figure
        x_pos, y_pos = self.position()
        self.set_X_Shape()
        print("X PLAYER(1):", x_pos, y_pos)
        self.goto(x_pos, y_pos)

    def set_O(self):
        # exchange the empty field to a 'O' figure
        x_pos, y_pos = self.position()
        self.set_O_Shape()
        print("O PLAYER(2):", x_pos, y_pos)
        self.goto((x_pos-RADIUS+RADIUS/5), y_pos)

    def reset_field(self):
        name = self.name
        x_pos = self.x_pos
        y_pos = self.y_pos
        self.__init__(name, x_pos, y_pos)

def createMyTurtles(fields):
    # creating all turtles and adding them to an array
    for i in range(9):
        name = fields[i]
        x_pos, y_pos = coordinates[i]
        my_turtle = MyTurtle(name, x_pos, y_pos)
        turtles.append(my_turtle)

def createCanvas(screen):
    # create the tictactoe field with an temporary turtle
    pen_bg = Turtle()
    pen_bg.speed(0)
    pen_bg.lt(90)
    pen_bg.pu()
    pen_bg.goto(-100, -300)
    pen_bg.pd()
    pen_bg.fd(600)
    pen_bg.pu()
    pen_bg.goto(100, -300)
    pen_bg.pd()
    pen_bg.fd(600)
    pen_bg.rt(90)
    pen_bg.pu()
    pen_bg.goto(-300, -100)
    pen_bg.pd()
    pen_bg.fd(600)
    pen_bg.pu()
    pen_bg.goto(-300, 100)
    pen_bg.pd()
    pen_bg.fd(600)
    pen_bg.hideturtle()

def playerMove(xdummy, ydummy):
    global player

    # set index start
    index = 0
    print("Clicked here:", xdummy, ydummy)
    # get index
    for start_x, start_y in coordinates:
        # compare xdummy and ydummy with coordinate list
        print(start_x, start_y)
        if start_x <= xdummy < start_x + 200 and start_y <= ydummy < start_y + 200:
            print("Found!", start_x, start_y)
            # chosen field was found
            if turtles[index].shape() != "square":
                # field was already chosen by a player
                print("Error! Field is already taken!")
            else:
                if player == 1:
                    # player: X
                    turtles[index].set_X()
                    checkWin(player)
                    player = 2
                else:
                    # player: O
                    turtles[index].set_O()
                    checkWin(player)
                    player = 1
            # move is finished so end function
            return 0

        # increase index every cycle
        index += 1

def checkWin(player):
    # the turtle_.shape() != "square" is to be sure the game isnt over if all positions are still empty "squares"
    if(turtles[0].shape() != "square" and turtles[0].shape() == turtles[4].shape()  and turtles[4].shape()  == turtles[8].shape()):     # oben rechts nach unten links
        winEvent(player)
    elif(turtles[2].shape() != "square" and turtles[2].shape() == turtles[4].shape() and turtles[6].shape() == turtles[4].shape()):   # oben links nach unten rechts
        winEvent(player)
    elif(turtles[2].shape() != "square" and turtles[2].shape() == turtles[5].shape() and turtles[8].shape() == turtles[5].shape()):   # obere reihe horizontal
        winEvent(player)
    elif (turtles[1].shape() != "square" and turtles[1].shape() == turtles[4].shape() and turtles[7].shape() == turtles[4].shape()):  # mittlere reihe horiz.
        winEvent(player)
    elif (turtles[0].shape() != "square" and turtles[0].shape() == turtles[3].shape() and turtles[6].shape() == turtles[3].shape()):  # untere reihe horiz.
        winEvent(player)
    elif (turtles[0].shape() != "square" and turtles[0].shape() == turtles[1].shape() and turtles[2].shape() == turtles[1].shape()):  # linke reihe vertik.
        winEvent(player)
    elif (turtles[3].shape() != "square" and turtles[3].shape() == turtles[4].shape() and turtles[5].shape() == turtles[4].shape()):  # mittlere reihe vertik.
        winEvent(player)
    elif (turtles[8].shape() != "square" and turtles[8].shape() == turtles[7].shape() and turtles[6].shape() == turtles[7].shape()):  # rechte reihe vertik.
        winEvent(player)

def winEvent(player):
    win_text = "Player " + str(player) + " won!"
    ctypes.windll.user32.MessageBoxW(0, win_text, "TicTacToe Info")
    quit()


def main(fields, screen):
    createMyTurtles(fields)
    createCanvas(screen)

    for i in range(9):
        turtles[i].onclick(playerMove)

    screen.onkeypress(quit, "Escape")       # Esc closes the programm


if __name__ == "__main__":
    main(fields, screen)
    screen.listen()
    screen.mainloop()
