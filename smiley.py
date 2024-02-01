"""Author: Dona Pal
   Date: 31/01/2024
   This program uses turtle to draw a smiley"""

# this code is complete
import turtle as t
t.pensize(2)

def draw_circle():
    t.up()
    t.goto(0,-200)
    t.down()
    t.fillcolor("gold")
    t.begin_fill()
    t.circle(200)
    t.end_fill()   

def nose():
    t.up()
    t.goto(0,0)
    t.forward(5)
    t.down()
    t.fillcolor("Pink")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def eyes():
    t.fillcolor("White")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.up()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.down()
    t.fillcolor("navy")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    t.fillcolor("Black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def smile():
    t.pensize(4)
    t.up()
    t.goto(100,-70)
    t.down()
    t.fillcolor("Black")
    t.begin_fill()
    t.left(180)
    t.forward(200)
    t.left(180)
    t.left(270)
    t.circle(100,180)
    t.end_fill()

def main():
    draw_circle()
    nose()
    t.up()
    t.goto(-75,40)
    t.down()
    eyes()
    t.up()
    t.goto(75,40)
    t.down()
    eyes()
    smile()
    
    input("enter")
    print(t.xcor())
    print(t.ycor())

main()
'''Code is
working'''