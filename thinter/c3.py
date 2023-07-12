from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("First Window")
window.geometry("350x200")
chk_state = BooleanVar()
chk_state.set(True) # Set check state
chk = Checkbutton(window, text="Choose")

chk.grid(column=0, row=0)
window.mainloop()