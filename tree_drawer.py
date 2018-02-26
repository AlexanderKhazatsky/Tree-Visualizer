import turtle as t
screen = t.Screen()

t.title ("Trees!")
t.speed(0)


def draw_leaf(label, position, radius=50):
    """Draws a circle with label written in the middle of it."""
    t.goto(*position)
    # FIXME: if text size is greater than 16 it goes out of the circle
    text_size =  18 // len(label) + 12
    t.color('Dark Blue')
    t.begin_fill()
    t.down()
    t.circle(radius,extent=None, steps=100)
    t.end_fill()
    t.up()
    t.hideturtle()
    t.penup()
    t.color('yellow')
    t.goto(position[0], position[1]+radius-(text_size//2))
    t.write(label, align='center', font = ('Times New Roman', text_size))
    t.goto(position[0], position[1])


draw_leaf("hello", [1,1], radius=50)