from tkinter import *

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)



window = Tk()
window.title("First Window")
window.geometry("500x500") #  设置窗口大小

"""
Label
# font 设置字体和大小
# bg fg 前景色，后景色
"""
lbl = Label(window, text="Hello",font=("Arial Bold",50),bg="orange", fg="red")
lbl.grid(column=0, row=0)
"""
定义点击按钮，绑定函数
"""
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

"""
文本框
"""
txt = Entry(window, width=10)
txt.grid(column=3, row=6)
txt.focus() # 可以直接在文本框中输入信息而不需要点击文本框


window.mainloop()  # mainloop函数，这个函数将让窗口等待用户与之交互，直到我们关闭它


