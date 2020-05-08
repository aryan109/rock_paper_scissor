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

options = ('rock', 'paper', 'scissor')
player_score = 0
computer_score = 0
computer_choice = 0
player_choice = 0


def set_rock():
    global player_choice
    player_choice = 0


def set_paper():
    global player_choice
    player_choice = 0


def set_scissor():
    global player_choice
    player_choice = 0


def submit_name():
    name = E1.get()
    label = Label(master, text="Hi {}, let's start the game!!!".format(name))
    label.grid(row=2)
    global options, player_score, computer_score


submit_button = Button(user_entry_frame, text="submit", command=submit_name)
submit_button.grid(row=0, column=2)

user_entry_frame.grid(row=1, column=0)

game_button_frame = Frame(master)
rock_button = Button(game_button_frame, text='ROCK', state=DISABLED)
rock_button.pack(side=LEFT)
rock_button = Button(game_button_frame, text='PAPER', state=DISABLED)
rock_button.pack(side=LEFT)
rock_button = Button(game_button_frame, text='SCISSOR', state=DISABLED)
rock_button.pack(side=LEFT)
game_button_frame.grid(row=3, column=0)

rock_button = Button(master, text='STOP', state=DISABLED)
rock_button.grid(row=4)
mainloop()
