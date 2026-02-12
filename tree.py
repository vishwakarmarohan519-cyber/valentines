import turtle

t = turtle.Turtle()
t.screen.bgcolor("black")
t.color("brown")
t.pensize(2)
t.left(90)
t.backward(100)
t.speed(0)

def tree(i):
    if i < 10:
        return
    t.forward(i)
    t.left(30)
    tree(i * 0.7)
    t.right(60)
    tree(i * 0.7)
    t.left(30)
    t.backward(i)

tree(100)
turtle.done()
