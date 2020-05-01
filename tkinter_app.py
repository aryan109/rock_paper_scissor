from tkinter import *

master = Tk()
master.title('Rock Paper Scissor')
master.geometry('600x600')

heading_frame = Frame(master)
heading_frame.pack()

text = Label(heading_frame, text="Welcome to rock paper scissor", font=('Comic Sans MS', 30))
text.pack()

username_frame = Frame(master)
L1 = Label(username_frame, text="User Name")
L1.pack(side=BOTTOM)
E1 = Entry(username_frame, bd=5)
E1.pack(side=BOTTOM)
username_frame.pack(side=LEFT)
mainloop()
