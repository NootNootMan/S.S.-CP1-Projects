import turtle  as t



t.color('#0345fc')
radius = 100
t.width(3)
t.speed(100)

while radius > 0:
    t.circle(radius)
    t.left(90)
    t.up()
    t.forward(5)  # Move inside to the next starting point
    t.down()
    t.right(90)
    radius -= 5
    t.shape("turtle")

t.done()