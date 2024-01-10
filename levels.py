from board import Board
from box import Box
from opening import Opening, UP, DOWN, LEFT, RIGHT
from cursor import Cursor

def getLevel(lvl):
    if (lvl == 1):
        return Board([[0,0,0],[0,0,0],[0,0,0]], [Box(2,1,0, LEFT, "blue"), Box(0,1,1, UP, "red")], Cursor(1,1))
    elif (lvl == 2):
        return Board([[0,0,0],[0,0,0],[0,0,0]], [Box(0,1,0, UP, "blue"), Box(2,1,1, LEFT, "red")], Cursor(1,1))
    elif (lvl == 3):
        return Board([[0,0,0],[0,0,0],[0,0,0]], [Box(1,1,0, UP, "blue"), Box(0,2,1, UP, "red"), Box(2,0,0, LEFT, "black")], Cursor(0,0))
    elif (lvl == 4):
        return Board([[0,0,0],[0,0,0],[0,0,0]], [Box(2,1,0, DOWN, "blue"), Box(0,1,1, RIGHT, "red"), Box(1,0,0, DOWN, "black"), Box(1,2,0, UP, "black")], Cursor(1,1))
    elif (lvl == 5):
        return Board([[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,0]], [Box(3,0,0, DOWN, "blue"), Box(2,1,1, RIGHT, "red"), Box(0,3,0, UP, "black"), Box(1,2,1, LEFT, "black")], Cursor(1,1))
    elif (lvl == 6):
        return Board([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], [Box(0,2,0, DOWN, "blue"), Box(1,1,1, LEFT, "red"), Box(1,0,0, DOWN, "black"), Box(3,1,0, LEFT, "black"), Box(2,3,0, UP, "black"), Box(2,1,1, UP, "black"), Box(2,1,1, RIGHT, "black"), Box(1,2,1, UP, "black")], Cursor(1,1))