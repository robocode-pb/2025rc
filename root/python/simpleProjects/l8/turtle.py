from cc import turtle
def dig(widht):
    for r in range(widht):
        digRow(widht)
def digRow(width):
    for r in range( width - 1):
        fuellevel = turtle.getFuelLevel()
        if fuellevel <=10:
            turtle.select(1)
            turtle.refuel(1)
        if turtle.detect():
            turtle.dig()
        turtle.forward()

side = "right"
def start():
    floors = int(input("floors = ?"))
    width = int(input("width = ?"))
    for i in range(floors):
        dig(width)
        turtle.turnRight()
        turtle.turnRight()
        if turtle.detectDown():
            turtle.digDown()
        turtle.down()
def turn():
    global side
    if side == ("right"):
        turtle.turnRight()
        if turtle.detect():
            turtle.dig()
        turtle.forward()
        turtle.turnRight()
        side = "left"
    else:
        turtle.turnLeft()
        if turtle.detect():
            turtle.dig()
        turtle.forward()
        turtle.turnLeft()
        side = "right"
