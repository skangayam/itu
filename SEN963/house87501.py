# File: house87501.py
# This program makes use of the graphics.py module to draw a simple landscape.

from graphics import *
win = GraphWin('House 87501')

def drawHouseBody():
    rect = Rectangle(Point(35, 130), Point(117,176))
    rect.draw(win)

def drawRoof():
    p = Polygon(Point(35,130),Point(25,130),Point(35,110),Point(117,110),Point(127,130),Point(117,130))
    p.draw(win)
    p.setOutline('brown')
    line = Line(Point(50,110), Point(50,100))
    line.draw(win)
    line = Line(Point(55,110), Point(55,100))
    line.draw(win)

def drawDoor():
    rect = Rectangle(Point(70,156), Point(82,176))
    rect.draw(win)
    rect.setOutline('blue')

def drawWindows():
    # Window 1
    rect = Rectangle(Point(45,140), Point(55,150))
    rect.draw(win)
    rect.setOutline('blue')
    line = Line(Point(45,145), Point(55,145))
    line.draw(win)
    line = Line(Point(50,150), Point(50,140))
    line.draw(win)
    # Window 2
    rect = Rectangle(Point(97,150), Point(107,140))
    rect.draw(win)
    rect.setOutline('blue')
    line = Line(Point(102,140), Point(102,150))
    line.draw(win)
    line = Line(Point(97,145), Point(107,145))
    line.draw(win)


def drawSun():
    line = Line(Point(132,18), Point(172,58))
    line.draw(win)
    line.setFill('red')
    line = Line(Point(132,58), Point(172,18))
    line.draw(win)
    line.setFill('red')
    line = Line(Point(152,0), Point(152,78))
    line.draw(win)
    line.setFill('red')
    line = Line(Point(112,38), Point(192,38))
    line.draw(win)
    line.setFill('red')
    circle = Circle(Point(152,38),20)
    circle.draw(win)
    circle.setFill('yellow')

def drawLandscape():
    line = Line(Point(150,176),Point(180,176))
    line.draw(win)
    line.setFill('brown')

def drawTree():
    rect = Rectangle(Point(160,176),Point(170,140))
    rect.draw(win)
    rect.setFill('brown')
    circle = Circle(Point(165,125),10)
    circle.draw(win)
    circle.setFill('green')
    circle = Circle(Point(160,135),10)
    circle.draw(win)
    circle.setFill('green')
    circle = Circle(Point(171,135),10)
    circle.draw(win)
    circle.setFill('green')

def getCoordinates():
    p = win.getMouse()
    print("You clicked", p.getX(), p.getY())

print("PYTHON_SEN963: Exercise3")
print("Submitted by: Shashi Kanth Kangayam")
print("ID: 87501")
drawHouseBody()
drawRoof()
drawDoor()
drawWindows()
drawSun()
drawLandscape()
drawTree()


input("Press Enter to continue...")


