import turtle
import random
from tkinter.simpledialog import *

inStr = ''
swidth, sheight = 300,300
tX, tY, txtSize = [0]*3

turtle.title('거북이로 글자 쓰기')
turtle.shape('turtle')
#.setup(wid,hei) 그래픽 창 크기를 설정
turtle.setup(width= swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()

#askstring tkinter의 들어있음, askstring('title','contents')
inStr = askstring('문자열 입력', '거북이 쓸 문자열 입력')

for ch in inStr:
    #-150~150 total 300
    tX = random.randrange(-swidth/2, swidth/2)
    tY = random.randrange(-sheight/2, sheight/2)
    red = random.random()
    blue = random.random()
    green = random.random()
    txtSize = random.randrange(10,50)
    
    turtle.goto(tX,tY)
    turtle.pencolor((red,green,blue))
    turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))

turtle.done()

