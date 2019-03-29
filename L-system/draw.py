"""
Uses a standard alphabet to draw L-systems. Currently understood symbols will
be defined here.
F - Draw forward by 1 unit distance
f - Draw forward by 1/2 unit distance
- - Turn left by 1 unit angle
+ - Turn right by 1 unit angle
[ - Save the current position and angle to a stack
] - Pop an angle and position from the stack
"""

import turtle


class L_system_image():
    def __init__(self, dist=16, angle=45):
        self.dist = dist
        # angle is given in degrees
        self.angle = angle

        self.stack = []

    def evaluate(self, c):
        if c == 'F':
            turtle.forward(self.dist)
        elif c == 'f':
            turtle.forward(self.dist/2)
        elif c == '-':
            turtle.left(self.angle)
        elif c == '+':
            turtle.right(self.angle)
        elif c == '[':
            self.stack.append((turtle.pos(), turtle.heading()))
        elif c == ']':
            turtle.penup()
            p, h = self.stack.pop()
            turtle.setpos(p[0], p[1])
            turtle.seth(h)
            turtle.pendown()

    def draw(self, s):
        turtle.hideturtle()
        # turtle.speed('fastest')
        turtle.tracer(False)
        turtle.left(90)
        turtle.penup()
        turtle.backward(100)
        turtle.pendown()

        for c in s:
            self.evaluate(c)

        turtle.exitonclick()


if __name__ == '__main__':
    L = L_system_image(dist=1)
    L.draw('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF[-FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF[-FFFFFFFFFFFFFFFF[-FFFFFFFF[-FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFFFFFF[-FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFFFFFFFFFFFFFF[-FFFFFFFF[-FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFFFFFF[-FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF[-FFFFFFFFFFFFFFFF[-FFFFFFFF[-FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFFFFFF[-FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFFFFFFFFFFFFFF[-FFFFFFFF[-FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFFFFFF[-FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f]+FFFF[-FF[-F[-f]+f]+F[-f]+f]+FF[-F[-f]+f]+F[-f]+f')
