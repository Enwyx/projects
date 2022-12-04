import os
os.system('cls' if os.name == 'nt' else 'clear')
import random
import time

board = [
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
]


def showBoard():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('-'*29)
    print(f'| {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]} | {board[0][5]} | {board[0][6]} |')
    print('-'*29)
    print(f'| {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]} | {board[1][5]} | {board[1][6]} |')
    print('-'*29)
    print(f'| {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]} | {board[2][5]} | {board[2][6]} |')
    print('-'*29)
    print(f'| {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]} | {board[3][5]} | {board[3][6]} |')
    print('-'*29)
    print(f'| {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]} | {board[4][5]} | {board[4][6]} |')
    print('-'*29)
    print(f'| {board[5][0]} | {board[5][1]} | {board[5][2]} | {board[5][3]} | {board[5][4]} | {board[5][5]} | {board[5][6]} |')
    print('-'*29)
    print('  1   2   3   4   5   6   7')

def getColumns():
    columns = [
        [board[0][0],board[1][0],board[2][0],board[3][0],board[4][0],board[5][0]],
        [board[0][1],board[1][1],board[2][1],board[3][1],board[4][1],board[5][1]],
        [board[0][2],board[1][2],board[2][2],board[3][2],board[4][2],board[5][2]],
        [board[0][3],board[1][3],board[2][3],board[3][3],board[4][3],board[5][3]],
        [board[0][4],board[1][4],board[2][4],board[3][4],board[4][4],board[5][4]],
        [board[0][5],board[1][5],board[2][5],board[3][5],board[4][5],board[5][5]],
        [board[0][6],board[1][6],board[2][6],board[3][6],board[4][6],board[5][6]],
    ]
    return columns

def getDiagonals():
    diagonals = [
        [board[2][0],board[3][1],board[4][2],board[5][3]],
        [board[1][0],board[2][1],board[3][2],board[4][3],board[5][4]],
        [board[0][0],board[1][1],board[2][2],board[3][3],board[4][4],board[5][5]],
        [board[0][1],board[1][2],board[2][3],board[3][4],board[4][5],board[5][6]],
        [board[0][2],board[1][3],board[2][4],board[3][5],board[4][6]],
        [board[0][3],board[1][4],board[2][5],board[3][6]],

        [board[3][0],board[2][1],board[1][2],board[0][3]],
        [board[4][0],board[3][1],board[2][2],board[1][3],board[0][4]],
        [board[5][0],board[4][1],board[3][2],board[2][3],board[1][4],board[0][5]],
        [board[5][1],board[4][2],board[3][3],board[2][4],board[1][5],board[0][6]],
        [board[5][2],board[4][3],board[3][4],board[2][5],board[1][6]],
        [board[5][3],board[4][4],board[3][5],board[2][6]],
    ]
    return diagonals

def addMove(move, player):
    columns = getColumns()
    if move.isnumeric():
        move = int(move) - 1
        if move <= 6 :
            depth = columns[move].count(' ') - 1
            if depth < 0 : 
                return 'error'
            else :
                board[depth][move] = player
                showBoard()
        else : return 'error'
    else : return 'error'



def isEnded(player):
    rows = board
    count = 0
    for row in rows:
        for i in row:
            if i == player : 
                count += 1
            else : count = 0
            if count >= 4 : 
                print(f'\n{player} won (row) {row}')
                return True
        count = 0

    columns = getColumns() 
    count = 0 
    for column in columns:
        for i in column:
            if i == player : 
                count += 1
                print(count)
            else : count = 0
            if count >= 4 : 
                print(f'\n{player} won (column) {column}')
                return True
        count = 0

    diagonals = getDiagonals()
    count = 0
    for diagonal in diagonals:
        for i in diagonal:
            if i == player : 
                count += 1
            else : count = 0
            if count >= 4 : 
                print(f'\n{player} won (diagonal) {diagonal}')
                return True
        count = 0
    
    spacesLeft = 0
    for i in board:
        spacesLeft += i.count(' ')
    if spacesLeft == 0:
        print('draw.')
        return True

    return False

def game():
    showBoard()
    turn = 0
    ended = False
    move = 0

    while ended == False:
        if turn == 0: player = 'X'
        else: player = 'O'
        
        move = input(' \n')
        #move = str(random.randint(1,7))
        if move == '!stop' : break
        else:
            move = addMove(move,player)
            if move == 'error': 
                showBoard()
            else : turn = not turn
            ended = isEnded(player)
        #time.sleep(0.01)



game()
