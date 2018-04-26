import turtle
def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)


def draw_square(some_turtle):
    cnt=1
    while cnt <=4:
        some_turtle.forward(100)
        some_turtle.right(90)
        cnt = cnt + 1

def draw_triangle():
    alan = turtle.Turtle()
    alan.color=("orange")
    cnt=1

    alan.forward(100)
    alan.right(120)
    alan.forward(100)
    alan.right(120)
    alan.forward(100)
    cnt = cnt + 1

def draw_flower():
    flower = turtle.Turtle()
    flower.color("blue")
    flower.shape('turtle')
    flower.speed(0)
    for i in range(1,46):
        flower.forward(150)
        flower.left(170)
    flower.left(180)
    flower.forward(100)

window = turtle.Screen()
window.bgcolor("red")
#brad = turtle.Turtle()
#brad.shape('turtle')
#brad.shapesize(2, 2)
#turtle.color("green")
#turtle.speed(1)

draw_flower()

#for i in range(1,30):
 #   draw_square(brad)
  #  brad.right(10)

#draw_triangle()

#draw_circle()


window.exitonclick()

