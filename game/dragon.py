import random
import time

def chooseCave():
    cave = ''

    while cave!='1' and cave!='2':
        print('which cave you prefer')
        cave = input()
    return cave

def checkCave(cave):
    friendlyCave = random.randint(1,2)
    print('You approach the cave ...')
    time.sleep(2)
    print('It is dark and spooky')
    time.sleep(2)
    print(str(friendlyCave))
    if cave == str(friendlyCave):
        print('you got the treasure')
    else:
        print('A dragon coming')

def Play():
    while True:
        cave = chooseCave()
        checkCave(cave)
        print('Do you want to play again?(Y or N):')
        playAgain = input('').upper()
        if playAgain == 'N':
            break

if __name__ == '__main__':
    Play()
