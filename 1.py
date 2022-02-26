from random import *
from tkinter import *
from math import *

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
    colors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
                  'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime', '#f55c4b'])
    x = 110 * cos(diapason)
    y = 80 * sin(diapason)
    canvas.create_line(x+300,y+300,x+301,y+301,fill='black')
    root.update()
    diapason += 0.01

canvas.mainloop()



