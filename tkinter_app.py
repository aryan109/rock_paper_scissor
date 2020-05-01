from tkinter import *

master = Tk()
master.title('Rock Paper Scissor')
master.geometry('300x300')

heading_frame = Frame(master)
heading_frame.pack()

text = Text(heading_frame)
text.insert(INSERT, "Welcome to rock paper scissor")
text.pack()

mainloop()
