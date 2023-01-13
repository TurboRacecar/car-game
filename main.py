import turtle
import time


wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(height=640, width=1000)
wn.tracer(0)
wn.title("Driving test by @TurboRacecar")

car = turtle.Turtle()
car.color("cyan")
car.speed(0)
car.shape("triangle")
car.penup()
car.state = "ready"
car.shapesize(stretch_len=2, stretch_wid=1)
car.moving = 0

def brakes():
    if car.moving > -16:
        car.moving -= 4


def forward():
    car.moving += 2


def right():
    car.right(10)


def left():
    car.left(10)


wn.listen()
wn.onkeypress(forward, "Up")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(brakes, "Down")

while True:
    wn.update()
    car.fd(car.moving)
    time.sleep(0.04)
