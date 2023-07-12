from tkinter import *
from time import strftime

root = Tk()
root.title("python时钟")

# 界面有多大，完全是靠字体撑起来的， 背景是黑色， 字体是白色
lbl = Label(root, font=("arial", 100, "bold"), bg="black", fg="white")
lbl.pack(anchor="center", fill="both", expand=1)

mode = 'hour'

def showtime():
    if mode == 'hour':
        string = strftime("%H:%M:%S %p")
    else:
        string = strftime("%Y-%m-%d")

    lbl.config(text=string)
    lbl.after(1000, showtime)       # 1秒钟以后执行time函数


def mouse_click(event):
    global mode
    if mode == 'hour':
        mode = 'day'
    else:
        mode = 'hour'


lbl.bind("<Button>", mouse_click)
showtime()

mainloop()