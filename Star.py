import turtle

windows = turtle.Screen()
t = turtle.Turtle()

windows.title("Star")
windows.setup(600, 800)
windows.bgcolor("white")


def star(size, angle, color="yellow"):
    t.color(color)
    t.begin_fill()

    t.left(angle)
    t.forward(size)

    t.right(72)
    t.forward(size)

    for _ in range(4):
        t.left(144)
        t.forward(size)

        t.right(72)
        t.forward(size)
    
    t.end_fill()


star(100, 20)

t.hideturtle()
windows.mainloop()
