import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

cherepaha = turtle.Turtle()
cherepaha.color('purple')
cherepaha.shape('turtle')
cherepaha.speed(10)
cherepaha.pensize(6)
cherepaha.down()

move = 90
angle = 72

for i in range(5):
    cherepaha.forward(move)
    cherepaha.stamp()
    cherepaha.right(angle)

wn.exitonclick()