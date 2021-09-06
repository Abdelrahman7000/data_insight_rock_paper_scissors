import random 

def play():
    user=input("Choose one==> 'r' for rock, 'p' for paper, 's' for scissors  ")
    computer=random.choice(['r','p','s'])

    if user==computer:
        print('computer\'s choice ==> ',computer)
        return 'tie'

    if is_win(user,computer):
        print('computer\'s choice ==> ',computer)
        return 'You win!'

    else:
        print('computer\'s choice ==> ',computer)
        return 'You lost'




def is_win(player,computer):
    ''' This function will return true if the player wins '''
    if (player=='r' and computer =='s') or (player =='s' and computer=='p') or (player =='p' and computer =='r'):
        return True


print(play())        