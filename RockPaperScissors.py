import random
import time

#👌 -> rock, ✌ -> scissors, 🙌 -> Scissors
moves = ['✌','🙌','👌']  

user = input('hi user.Whats your name?\n')

def play():
    time.sleep(2)
    print('ready.....')
    time.sleep(2)
    print(random.choice(moves))
    
points = 1
while points <= 3:
    play()
    print('Score is ',points,sep=' ')
    point_claim = input("Did you win/lose the move? If Yes press True else False:\t")
    if  point_claim == 'True':
        points += 1
    elif point_claim == 'False': points -= 1
    else:
        pass
            
print('You Win',user,'!',sep=' ')
