import turtle
import time

is_running = True

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(height=642, width=1200)
wn.tracer(0)
wn.title("Driving test")

car = turtle.Turtle()
car.color("cyan")
car.speed(0)
car.shape("triangle")
car.penup()
car.state = "ready"
car.shapesize(stretch_len=2, stretch_wid=1)
car.moving = 0
car.goto(-200, 100)

car2 = turtle.Turtle()
car2.color("orange")
car2.speed(0)
car2.shape("triangle")
car2.penup()
car2.state = "ready"
car2.shapesize(stretch_len=2, stretch_wid=1)
car2.moving = 0
car2.goto(-200, -100)


def brakes():
    if car.moving >= 8:
        car.moving -= 8
    else:
        car.moving = 0


def forward():
    if car.moving < 24:
        car.moving += 2


def right():
    car.right(10)


def left():
    car.left(10)


def reverse():
    if car.moving > -4:
        car.moving -= 2


def pause():
    global is_running
    if is_running:
        is_running = False
    else:
        is_running = True


def brakes2():
    if car2.moving >= 8:
        car2.moving -= 8
    else:
        car2.moving = 0


def forward2():
    if car2.moving < 24:
        car2.moving += 2


def right2():
    car2.right(10)


def left2():
    car2.left(10)


def reverse2():
    if car2.moving > -4:
        car2.moving -= 2


wn.listen()
wn.onkeypress(forward, "Up")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(brakes, "Down")
wn.onkeypress(pause, "q")
wn.onkeypress(reverse, "r")
wn.onkeypress(forward2, "w")
wn.onkeypress(left2, "a")
wn.onkeypress(right2, "d")
wn.onkeypress(brakes2, "s")
wn.onkeypress(reverse2, "x")


while True:
    if is_running:
        wn.update()
        car.fd(car.moving)
        car2.fd(car2.moving)
        time.sleep(0.04)
    else:
        wn.update()
