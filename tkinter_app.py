from tkinter import *

master = Tk()
master.title('Rock Paper Scissor')
master.geometry('600x600')

heading_frame = Frame(master)
heading_frame.pack()

text = Text(heading_frame, font=('Comic Sans MS', 30))
text.insert(INSERT, "Welcome to rock paper scissor")
text.pack()

mainloop()
