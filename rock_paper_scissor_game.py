import math
import random

in_one = input('\033[1;30;42mVOCÊ:\033[m')
possibilities = ['pedra', 'papel','tesoura']
SKYNET = (random.choice(possibilities))
if in_one == 'pedra' or 'papel' or 'tesoura':
    print('\033[1;30;41mSKYNET:\033[m',SKYNET)
    if in_one == 'pedra' and SKYNET == 'tesoura':
        print('YOU WIN!')
    if in_one == 'tesoura' and SKYNET == 'pedra':
        print('\033[30;41mYOU LOSE HUMAN!!!!') 
    if in_one == 'pedra' and SKYNET == 'papel':
        print('YOU LOSE!!!')
    if in_one == 'papel' and SKYNET == 'pedra':
        print('YOU WON!')
    if in_one == 'papel' and SKYNET == 'tesoura':
        print('YOU LOSE!!!!')
    if in_one == 'tesoura' and SKYNET == 'papel':
        print('YOU WON!')
    if in_one == SKYNET:
        print('DRAW GAME')
    
