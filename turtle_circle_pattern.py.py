import turtle
t = turtle
t.speed(30)
t.hideturtle()
for r in range(50,101,5):
    if r % 10 != 0:
        t.color('Red')
    else:
        t.color('Blue')
    t.penup()
    t.right(90)
    t.forward(5)
    t.left(90)
    t.pendown()
    t.circle(r)
t.exitonclick()


