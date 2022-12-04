import os
os.system('cls' if os.name == 'nt' else 'clear')

board = [
    [' ' , ' ' , ' '],
    [' ' , ' ' , ' '],
    [' ' , ' ' , ' '],
]

def showBoard():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'*3)
    print(f'1     {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print('    ', '-'*11)
    print(f'2     {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('    ', '-'*11)
    print(f'3     {board[2][0]} | {board[2][1]} | {board[2][2]}')
    print('\n      A   B   C')

def addMove(move, player):
    move = list(move)
    if len(move) != 2 : return 'error' 
    else :
        if move[0].upper() == 'A': column = 0
        elif move[0].upper() == 'B': column = 1
        elif move[0].upper() == 'C': column = 2
        else : return 'error'

        if move[1].isnumeric():
            row = int(move[1]) - 1
        else : return 'error'
        if row < 0 or row > 2 : return 'error'
        else : 
            if board[row][column] == ' ':
                board[row][column] = player
                showBoard()
            else : return 'error'

def isEnded(player):
    rows = board
    for i in rows:
        if i.count(player) == 3: 
            print(f'\n{player} won')
            return True
    
    columns = [
        [board[0][0],board[1][0],board[2][0]],
        [board[0][1],board[1][1],board[2][1]],
        [board[0][2],board[1][2],board[2][2]],
    ]
    for i in columns:
        if i.count(player) == 3: 
            print(f'\n{player} won')
            return True
    diagonals = [
        [board[0][0],board[1][1],board[2][2]],
        [board[2][0],board[1][1],board[0][2]],
    ]
    for i in diagonals:
        if i.count(player) == 3: 
            print(f'\n{player} won')
            return True

    emptySpaces = 0
    for i in board:
        emptySpaces += i.count(' ')
    if emptySpaces == 0 :
        print('\ndraw.')
        return True

    return False

def game():
    showBoard()
    turn = 0
    ended = False

    while ended == False:
        if turn == 0: player = 'X'
        else : player = 'O'
        
        move = input(' \n')
        if move == '!stop' : break
        else :
            move = addMove(move,player)
            if move == 'error' : 
                showBoard()
            else : turn = not turn
            ended = isEnded(player)

game()
