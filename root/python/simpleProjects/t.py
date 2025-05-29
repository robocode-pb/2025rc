from cc import turtle
fuel = turtle.getFuelLevel()
print("Fuel Levelоооолд "+str(fuel))
turtle.refuel(1)

kroki = 8
for i in range(kroki):
    if turtle.detectDown():
        turtle.digDown()
    turtle.turnRight()
    turtle.forward()
    # кожний 4 крок перемістtитись внмз
    if (i+1)%4 == 0: #кожний 4 крок
        turtle.down()

for i in range(kroki):
    turtle.up()

for комірка in range(2,16):
    turtle.select(комірка)
    turtle.drop()