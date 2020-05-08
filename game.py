import random

options = ('rock', 'paper', 'scissor')
player_score = 0
computer_score = 0
while True:
    comp_choice = random.choice(options)
    player_choice = input('enter your choice(type exit to exit)')
    if player_choice == 'exit':
        print('Game Finished')
        break
    if player_choice not in options:
        print('invalid choice, try again')
        continue
    pi = options.index(player_choice)
    ci = options.index(comp_choice)
    diff = pi - ci
    if diff is 0:
        print('Draw, computer chose {} and you chose {}'.format(comp_choice, player_choice))
        continue
    if pi is (ci + 1) % 3:
        print('Congratulations, you won computer chose {} you chose {}'.format(comp_choice, player_choice))
        player_score += 1
        continue
    else:
        print('Sorry, you lost computer chose {} you chose {}'.format(comp_choice, player_choice))
        computer_score += 1
print(' final scores:-\nplayer {}\ncomputer {}'.format(player_score, computer_score))
if player_score > computer_score:
    print('Congratulations, you are a champion')
elif player_score == computer_score:
    print('Draw.')
else:
    print('Booo, you lost')
