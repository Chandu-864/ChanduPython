
from graphics import*

def main():

    win =GraphWin("MyCircle", 100,100)

    c =Circle(Point(50,50),10)

    c.draw(win)

    win.getMouse()# pausefor clickin window

    win.close()

main()