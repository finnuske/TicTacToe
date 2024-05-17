from turtle import Turtle, Screen
import time
import ctypes


fields = [("A1", -300, -200),("A2", -300, 0),("A3",-300,200 ), ("B1", -100, -200), ("B2",-100,0), ("B3",-100,200), ("C1",100,-200), ("C2",100,0),("C3",100,200)]
# field gives an array with each a tuple with the: 'name', x_pos, y_pos for creating all the 9 field spots
turtles = []

SIZE = 600
RADIUS = SIZE/6
player = 1          # player 1 is: X; player 2 is: O

screen = Screen()
screen.setup(SIZE, SIZE)
screen.title("TicTacToe by Finn Wulff")


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
        self.goto((x_pos+100), y_pos)

    def set_O_Shape(self, xdummy, ydummy):
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

    def set_X_Shape(self, xdummy, ydummy):
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

    def set_X(self, xdummy, ydummy):
        # exchange the empty field to a 'X' figure
        x_pos, y_pos = self.position()
        self.set_X_Shape(xdummy, ydummy)
        print(x_pos, y_pos)
        self.goto(x_pos, y_pos)

    def set_O(self, xdummy, ydummy):
        # exchange the empty field to a 'O' figure
        x_pos, y_pos = self.position()
        self.set_O_Shape(xdummy, ydummy)
        print(x_pos, y_pos)
        self.goto((x_pos-RADIUS+RADIUS/5), y_pos)

    def reset_field(self):
        name = self.name
        x_pos = self.x_pos
        y_pos = self.y_pos
        self.__init__(name, x_pos, y_pos)

def createMyTurtles(fields):
    # creating all turtles and adding them to an array
    for i in range(9):
        name, x_pos, y_pos = fields[i]
        my_turtle = MyTurtle(name, x_pos, y_pos)
        turtles.append(my_turtle)

def createCanvas(screen):
    # create the tictactoe field with an temporary turtle
    pen_temp = Turtle()
    pen_temp.speed(0)
    pen_temp.lt(90)
    pen_temp.pu()
    pen_temp.goto(-100, -300)
    pen_temp.pd()
    pen_temp.fd(600)
    pen_temp.pu()
    pen_temp.goto(100, -300)
    pen_temp.pd()
    pen_temp.fd(600)
    pen_temp.rt(90)
    pen_temp.pu()
    pen_temp.goto(-300, -100)
    pen_temp.pd()
    pen_temp.fd(600)
    pen_temp.pu()
    pen_temp.goto(-300, 100)
    pen_temp.pd()
    pen_temp.fd(600)
    pen_temp.hideturtle()

def playerMove_A1(xdummy, ydummy):
    global player

    if turtle_A1.shape() != "square":
        print("Error! Field is already taken!")
    else:
        if player == 1:
            turtle_A1.set_X(xdummy, ydummy)
            check_win(player)
            player = 2
        elif player == 2:
            turtle_A1.set_O(xdummy, ydummy)
            check_win(player)
            player = 1
        else:
            print("Error! Player out of range:", player)
        # check win statement

def playerMove_A2(xdummy, ydummy):
    global player

    if turtle_A2.shape() != "square":
        print("Error! Field is already taken!")
    else:
        if player == 1:
            turtle_A2.set_X(xdummy, ydummy)
            check_win(player)
            player = 2
        elif player == 2:
            turtle_A2.set_O(xdummy, ydummy)
            check_win(player)
            player = 1
        else:
            print("Error! Player out of range:", player)
        # check win statement

def playerMove_A3(xdummy, ydummy):
    global player

    if turtle_A3.shape() != "square":
        print("Error! Field is already taken!")
    else:
        if player == 1:
            turtle_A3.set_X(xdummy, ydummy)
            check_win(player)
            player = 2
        elif player == 2:
            turtle_A3.set_O(xdummy, ydummy)
            check_win(player)
            player = 1
        else:
            print("Error! Player out of range:", player)
        # check win statement

def playerMove_B1(xdummy, ydummy):
    global player

    if turtle_B1.shape() != "square":
        print("Error! Field is already taken!")
    else:
        if player == 1:
            turtle_B1.set_X(xdummy, ydummy)
            check_win(player)
            player = 2
        elif player == 2:
            turtle_B1.set_O(xdummy, ydummy)
            check_win(player)
            player = 1
        else:
            print("Error! Player out of range:", player)
        # check win statement

def playerMove_B2(xdummy, ydummy):
    global player

    if turtle_B2.shape() != "square":
        print("Error! Field is already taken!")
    else:
        if player == 1:
            turtle_B2.set_X(xdummy, ydummy)
            check_win(player)
            player = 2
        elif player == 2:
            turtle_B2.set_O(xdummy, ydummy)
            check_win(player)
            player = 1
        else:
            print("Error! Player out of range:", player)
        # check win statement

def playerMove_B3(xdummy, ydummy):
    global player

    if turtle_B3.shape() != "square":
        print("Error! Field is already taken!")
    else:
        if player == 1:
            turtle_B3.set_X(xdummy, ydummy)
            check_win(player)
            player = 2
        elif player == 2:
            turtle_B3.set_O(xdummy, ydummy)
            check_win(player)
            player = 1
        else:
            print("Error! Player out of range:", player)
        # check win statement

def playerMove_C1(xdummy, ydummy):
    global player

    if turtle_C1.shape() != "square":
        print("Error! Field is already taken!")
    else:
        if player == 1:
            turtle_C1.set_X(xdummy, ydummy)
            check_win(player)
            player = 2
        elif player == 2:
            turtle_C1.set_O(xdummy, ydummy)
            check_win(player)
            player = 1
        else:
            print("Error! Player out of range:", player)
        # check win statement

def playerMove_C2(xdummy, ydummy):
    global player

    if turtle_C2.shape() != "square":
        print("Error! Field is already taken!")
    else:
        if player == 1:
            turtle_C2.set_X(xdummy, ydummy)
            check_win(player)
            player = 2
        elif player == 2:
            turtle_C2.set_O(xdummy, ydummy)
            check_win(player)
            player = 1
        else:
            print("Error! Player out of range:", player)
        # check win statement

def playerMove_C3(xdummy, ydummy):
    global player

    if turtle_C3.shape() != "square":
        print("Error! Field is already taken!")
    else:
        if player == 1:
            turtle_C3.set_X(xdummy, ydummy)
            check_win(player)
            player = 2
        elif player == 2:
            turtle_C3.set_O(xdummy, ydummy)
            check_win(player)
            player = 1
        else:
            print("Error! Player out of range:", player)
        # check win statement

def check_win(player):
    if player == 1:
        # check for X row
        if(turtle_A1.shape() == "X" and turtle_B2.shape() == "X" and turtle_C3.shape() == "X"):     # oben rechts nach unten links
            win_event(player)
        elif(turtle_A3.shape() == "X" and turtle_B2.shape() == "X" and turtle_C1.shape() == "X"):   # oben links nach unten rechts
            win_event(player)
        elif(turtle_A3.shape() == "X" and turtle_B3.shape() == "X" and turtle_C3.shape() == "X"):   # obere reihe horizontal
            win_event(player)
        elif (turtle_A2.shape() == "X" and turtle_B2.shape() == "X" and turtle_C2.shape() == "X"):  # mittlere reihe horiz.
            win_event(player)
        elif (turtle_A1.shape() == "X" and turtle_B1.shape() == "X" and turtle_C1.shape() == "X"):  # untere reihe horiz.
            win_event(player)
        elif (turtle_A1.shape() == "X" and turtle_A2.shape() == "X" and turtle_A3.shape() == "X"):  # linke reihe vertik.
            win_event(player)
        elif (turtle_B1.shape() == "X" and turtle_B2.shape() == "X" and turtle_B3.shape() == "X"):  # mittlere reihe vertik.
            win_event(player)
        elif (turtle_C3.shape() == "X" and turtle_C2.shape() == "X" and turtle_C1.shape() == "X"):  # rechte reihe vertik.
            win_event(player)

    elif player == 2:
        # check for O row
        if (turtle_A1.shape() == "O" and turtle_B2.shape() == "O" and turtle_C3.shape() == "O"):  # oben rechts nach unten links
            win_event(player)
        elif (turtle_A3.shape() == "O" and turtle_B2.shape() == "O" and turtle_C1.shape() == "O"):  # oben links nach unten rechts
            win_event(player)
        elif (turtle_A3.shape() == "O" and turtle_B3.shape() == "O" and turtle_C3.shape() == "O"):  # obere reihe horizontal
            win_event(player)
        elif (turtle_A2.shape() == "O" and turtle_B2.shape() == "O" and turtle_C2.shape() == "O"):  # mittlere reihe horiz.
            win_event(player)
        elif (turtle_A1.shape() == "O" and turtle_B1.shape() == "O" and turtle_C1.shape() == "O"):  # untere reihe horiz.
            win_event(player)
        elif (turtle_A1.shape() == "O" and turtle_A2.shape() == "O" and turtle_A3.shape() == "O"):  # linke reihe vertik.
            win_event(player)
        elif (turtle_B1.shape() == "O" and turtle_B2.shape() == "O" and turtle_B3.shape() == "O"):  # mittlere reihe vertik.
            win_event(player)
        elif (turtle_C3.shape() == "O" and turtle_C2.shape() == "O" and turtle_C1.shape() == "O"):  # rechte reihe vertik.
            win_event(player)
    else:
        print("Error! Player out of range:", player)

def win_event(player):
    win_text = "Player " + str(player) + " won!"
    ctypes.windll.user32.MessageBoxW(0, win_text, "TicTacToe Info")
    quit()


def main(fields, screen):
    global turtle_A1,turtle_A2,turtle_A3,turtle_B1,turtle_B2,turtle_B3,turtle_C1,turtle_C2,turtle_C3

    createMyTurtles(fields)
    createCanvas(screen)

    turtle_A1 = turtles[0]
    turtle_A2 = turtles[1]
    turtle_A3 = turtles[2]
    turtle_B1 = turtles[3]
    turtle_B2 = turtles[4]
    turtle_B3 = turtles[5]
    turtle_C1 = turtles[6]
    turtle_C2 = turtles[7]
    turtle_C3 = turtles[8]

    turtle_A1.onclick(playerMove_A1)
    turtle_A2.onclick(playerMove_A2)
    turtle_A3.onclick(playerMove_A3)
    turtle_B1.onclick(playerMove_B1)
    turtle_B2.onclick(playerMove_B2)
    turtle_B3.onclick(playerMove_B3)
    turtle_C1.onclick(playerMove_C1)
    turtle_C2.onclick(playerMove_C2)
    turtle_C3.onclick(playerMove_C3)

    screen.onkeypress(quit, "Escape")       # Esc closes the programm


if __name__ == "__main__":
    main(fields, screen)
    screen.listen()
    screen.mainloop()
