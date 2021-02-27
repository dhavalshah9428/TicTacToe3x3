import numpy as ny
import random

GameBoard = ny.array([['/','/','/'], ['/','/','/'], ['/','/','/']])

def xsturn():
    row = int(input('X, which row?'))
    place = int(input('X, which place?'))
    if GameBoard[row][place] == '/':
        GameBoard[row][place] = 'X'
    else:
        print ('Move not possible!')
        xsturn()
    
def osturn():
    row = random.randint(0,2)
    place = random.randint(0,2)
    if GameBoard[row][place] == '/':
        GameBoard[row][place] = 'O'
    else:
        osturn()

def win():
    value = 0
    if GameBoard[0][0] == GameBoard[0][1] == GameBoard[0][2]:
        if GameBoard[0][0] != '/':
            value += 1
    elif GameBoard[1][0] == GameBoard[1][1] == GameBoard[1][2]:
        if GameBoard[1][0] != '/':
            value += 1
    elif GameBoard[2][0] == GameBoard[2][1] == GameBoard[2][2]:
        if GameBoard[2][0] != '/':
            value += 1
    elif GameBoard[0][0] == GameBoard[1][0] == GameBoard[2][0]:
        if GameBoard[0][0] != '/':
            value += 1
    elif GameBoard[0][1] == GameBoard[1][1] == GameBoard[2][1]:
        if GameBoard[0][1] != '/':
            value += 1
    elif GameBoard[0][2] == GameBoard[1][2] == GameBoard[2][2]:
        if GameBoard[0][2] != '/':
            value += 1
    elif GameBoard[0][0] == GameBoard[1][1] == GameBoard[2][2]:
        if GameBoard[0][0] != '/':
            value += 1
    elif GameBoard[0][2] == GameBoard[1][1] == GameBoard[2][0]:
        if GameBoard[0][2] != '/':
            value += 1
    return value

def game():
    GamePlay = 0
    while win() == 0:

        xsturn()
        GamePlay += 1
        if win() == 1:
            print(ny.matrix(GameBoard))
            print('X won the game!')
            break
        if GamePlay ==9 : 
            print('Game draw !')
            break

        osturn()
        GamePlay += 1
        print('\n Current board')
        if win() == 1:
            print(ny.matrix(GameBoard))
            print('O won the game!')
            break

        print(ny.matrix(GameBoard))

game()