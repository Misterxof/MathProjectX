from random import *
from tkinter import *
from math import *
import time

size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()
diapason = 0
x1 = 190
y1 = 220
x2 = 410
y2 = 380
canvas.create_oval(x1,y1,x2,y2,fill='blue')
canvas.create_line(x1,y1,x1+1,y1+1,fill='black')
canvas.create_line(x2,y2,x2+1,y2+1,fill='black')
canvas.create_line(x2,y2,x1,y1,fill='red')
canvas.create_line(x2,y1,x1,y2,fill='red')

while diapason < 2*pi:
    x = 110 * cos(diapason)
    y = 80 * sin(diapason)
    canvas.create_line(x+300,y+300,x+301,y+301,fill='black')
    root.update()
    diapason += 0.01

t = 0

print(round(time.time()))

tc = round(time.time())
tp = round(time.time())
while True:
    tc = round(time.time())
    if (tc - tp == 1):
        canvas.delete("p")
        tp = round(time.time())
        if (t <= -2*pi):
            t = 0
        else:
            t -= 0.1
    
    xp = 110 * cos(t)
    yp = 80 * sin(t)
    canvas.create_oval(xp+280, yp+280, xp+320, yp+320, outline="green", fill="yellow", tags="p")
    root.update()

    

canvas.mainloop()



