from tkinter import *
import random

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

player_score = 0
computer_score = 0
computer_choice = 0
player_choice = 0
flag = 1

step_result = "step_result"
res_label = Label(master, text=step_result)
res_label.grid(row=5)


def set_rock():
    global player_choice, flag
    if flag == 1:
        player_choice = 'rock'
        start_game()
    return


def set_paper():
    global player_choice, flag
    if flag == 1:
        player_choice = 'paper'
        start_game()
    return


def set_scissor():
    global player_choice, flag
    if flag == 1:
        player_choice = 'scissor'
        start_game()
    return


def start_game():
    global computer_choice, computer_score, player_choice, player_score, res_label, step_result
    options = ('rock', 'paper', 'scissor')
    computer_choice = random.choice(options)
    pi = options.index(player_choice)
    ci = options.index(computer_choice)
    diff = pi - ci
    if diff is 0:
        print('Draw, computer chose {} and you chose {}'.format(computer_choice, player_choice))  # fixme remove print
        step_result = 'Draw, computer chose {} and you chose {}'.format(computer_choice, player_choice)

    elif pi is (ci + 1) % 3:
        print('Congratulations, you won computer chose {} you chose {}'.format(computer_choice, player_choice))
        step_result = 'Congratulations, you won computer chose {} you chose {}'.format(computer_choice, player_choice)
        player_score += 1
    else:
        print('Sorry, you lost computer chose {} you chose {}'.format(computer_choice, player_choice))
        step_result = 'Sorry, you lost computer chose {} you chose {}'.format(computer_choice, player_choice)
        computer_score += 1
    # print(f'computer score{computer_score}, player score{player_score}')
    res_label.config(text=step_result)
    return


def end_game():
    global computer_score, player_score, res_label
    if player_score > computer_score:
        print('Congratulations, you are a champion')
        # res_label = 'Congratulations, you are a champion'
    elif player_score == computer_score:
        print('Draw.')
    else:
        print('Booo, you lost')


def submit_name():
    name = E1.get()
    label = Label(master, text="Hi {}, let's start the game!!!".format(name))
    label.grid(row=2)
    global options, player_score, computer_score


submit_button = Button(user_entry_frame, text="submit", command=submit_name)
submit_button.grid(row=0, column=2)

user_entry_frame.grid(row=1, column=0)
game_button_frame = Frame(master)
rock_button = Button(game_button_frame, text='ROCK', command=set_rock)
rock_button.pack(side=LEFT)
rock_button = Button(game_button_frame, text='PAPER', command=set_paper)
rock_button.pack(side=LEFT)
rock_button = Button(game_button_frame, text='SCISSOR', command=set_scissor)
rock_button.pack(side=LEFT)
game_button_frame.grid(row=3, column=0)

rock_button = Button(master, text='STOP', command=end_game)
rock_button.grid(row=4)
mainloop()
