import turtle
tao = turtle.Pen()
tao.shape("turtle")

def rectangle() :
    for i in range (4):
        tao.forward(200)
        tao.left(90)
rectangle()

def go(x,y) :
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
go(-200,200)

rectangle()
go(-200,-200)
rectangle()

tao.left(90)
tao.forward(400)
    
