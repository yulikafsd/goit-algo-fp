import turtle

recur_depth = int(input("Plese choose the depth: "))

screen = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.up()
t.setpos(0, -200)
t.left(90)
t.down()


def pythagoras_tree(length, depth):
    if depth == 0:
        t.forward(length)
        return

    t.forward(length)

    # Зберігаємо позицію та кут
    pos = t.position()
    heading = t.heading()

    # Ліва гілка
    t.left(45)
    pythagoras_tree(length * 0.65, depth - 1)

    # Відновлюємо позицію і кут перед правою гілкою
    t.setpos(pos)
    t.setheading(heading)

    # Права гілка
    t.right(45)
    pythagoras_tree(length * 0.65, depth - 1)

    # Повертаємося назад після обох гілок
    t.setpos(pos)
    t.setheading(heading)


if __name__ == "__main__":
    pythagoras_tree(150, recur_depth)
    screen.mainloop()
