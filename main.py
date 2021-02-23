row1 = ['/','/','/']
row2 = ['/','/','/']
row3 = ['/','/','/']

def xsturn():
    row = input('X, which row?')
    place = input('X, which place?') - 1
    if row == 1:
        if row1[place] == '/':
            row1[place] = 'X'
        else:
            print ('Move not possible!')
            xsturn()
    elif row == 2:
        if row2[place] == '/':
            row2[place] = 'X'
        else:
            print ('Move not possible!')
            xsturn()
    elif row == 3:
        if row3[place] == '/':
            row3[place] = 'X'
        else:
            print ('Move not possible!')
            xsturn()

def osturn():
    row = input('O, which row?')
    place = input('O, which place?') - 1
    if row == 1:
        if row1[place] == '/':
            row1[place] = 'O'
        else:
            print ('Move not possible!')
            osturn()
    elif row == 2:
        if row2[place] == '/':
            row2[place] = 'O'
        else:
            print ('Move not possible!')
            osturn()
    elif row == 3:
        if row3[place] == '/':
            row3[place] = 'O'
        else:
            print ('Move not possible!')
            osturn()

def win():
    value = 0
    if row1[0] == row1[1] == row1[2]:
        if row1[0] != '/':
            value += 1
    elif row2[0] == row2[1] == row2[2]:
        if row2[0] != '/':
            value += 1
    elif row3[0] == row3[1] == row3[2]:
        if row3[0] != '/':
            value += 1
    elif row1[0] == row2[0] == row3[0]:
        if row1[0] != '/':
            value += 1
    elif row1[1] == row2[1] == row3[1]:
        if row1[1] != '/':
            value += 1
    elif row1[2] == row2[2] == row3[2]:
        if row1[2] != '/':
            value += 1
    elif row1[0] == row2[1] == row3[2]:
        if row1[0] != '/':
            value += 1
    elif row1[2] == row2[1] == row3[0]:
        if row1[2] != '/':
            value += 1
    return value

def printingrows():
    print (row1)
    print (row2)
    print (row3)

def game():
    while win() == 0:
        xsturn()
        printingrows()
        if win() == 1:
            print ('X won the game!')
            break
        else:
            osturn()
            printingrows()
            if win() == 1:
                print('O won the game!')
                break
game()