import turtle

def main():
    scr = turtle.getscreen()
    scr.setup(width=.3, height=.9, startx=10, starty=10)
    scr.title("Dastardly Flying Turtles")
    scr.bgcolor("black")

    t = turtle.Turtle()

    t.color("white", "purple")
    t.pensize(3)
    t.shape("turtle")

    for i in range(5):
        t.forward(50)
        t.right(144)

    turtle.done()

if __name__ == "__main__":
    main()
