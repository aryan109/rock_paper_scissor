from tkinter import *

master = Tk()
master.title('Rock Paper Scissor')
canvas_height = 600
canvas_width = 400
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)
mainloop()
