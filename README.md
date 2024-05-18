# TicTacToe 

A simple Tic Tac Toe Game with player 1: X and player 2: O.
This was one of my first bigger programming projects. I wrote it when 
I first started learning to code. I found the 'turtle' library and though
it was cool to create a game with it. 

# Program
Every field gets a turtle objects which is saved in an array called 'turtles'.
The turtle is scaled to the size of a field then the function 'playerMove' is called 
if the player clicks on a field. In every player move the checkWin functions is called.
(This function still needs a bit of rework)

# Changes
The program had a lot of unnecessary code (probably still has) that I fixed.

- win conditions were double for each player, which is now at least for each player the same statements
- saved all of the turtles in an array instead of initializing a variable for each
- created one function for a player move instead of a function for each field (lol)
  - for that the program searches for the right field with the given coordinates from the player input on 'screen'
