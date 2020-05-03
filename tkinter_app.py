from tkinter import *

master = Tk()
master.title('Rock Paper Scissor')
master.geometry('600x600')

text = Label(master, text="Welcome to rock paper scissor", font=('Comic Sans MS', 30))
text.grid(row=0)

user_entry_frame = Frame(master)
L1 = Label(user_entry_frame, text="Enter Name")
L1.grid(row=0, column=0)

E1 = Entry(user_entry_frame, bd=5)
E1.grid(row=0, column=1)


def submit_name():
    name = E1.get()
    label = Label(master, text="Hi {}, let's start the game!!!".format(name))
    label.grid(row=2)


submit_button = Button(user_entry_frame, text="submit", command=submit_name)
submit_button.grid(row=0, column=2)

user_entry_frame.grid(row=1, column=0)

game_button_frame = Frame(master)
rock_button = Button(game_button_frame, text='ROCK', state=DISABLED)
rock_button.pack()
rock_button = Button(game_button_frame, text='PAPER', state=DISABLED)
rock_button.pack()
rock_button = Button(game_button_frame, text='SCISSOR', state=DISABLED)
rock_button.pack()
rock_button = Button(game_button_frame, text='STOP', state=DISABLED)
rock_button.pack()
game_button_frame.grid(row=6, column=0)

mainloop()
