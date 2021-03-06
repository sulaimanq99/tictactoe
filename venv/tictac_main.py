import random

def new_board():
    board = []
    for i in range(0,3):
        board.append([None,None,None])
    return board

def render(board):
    print('  0 1 2 \n -------')
    for i in range(3):
        grid = [x if x else ' ' for x in board[i]]
        print(str(i)+'|'+' '.join(grid) + '|')
    print(' -------')

def get_move(player_token):
    print(player_token + "'s turn")
    X = int(input('Enter your moves x coordinate: '))
    Y = int(input('Enter your moves y coordinate: '))
    player_move = (X,Y)
    return player_move

def make_move(board,player_move,player_token):
    x = player_move[0]
    y = player_move[1]

    if is_legal_move(board,player_move):
        board[y][x] = player_token
    else:
        print(str(player_move) + ' is already taken, please try again')
        player_move = get_move(player_token)
        return make_move(board, player_move, player_token)
    return board

def is_legal_move(board,player_move):
    x = player_move[0]
    y = player_move[1]
    if not board[y][x]:
        return True
    else:
        return False

def game_loop():
    board = new_board()
    players = {1:'X', -1:'O'}
    player_key = 1
    render(board)
    while True:
        player = players[player_key]
        move = get_move(player)
        board = make_move(board, move, player)
        render(board)
        player_key *= -1
        #check_winner(board, move_count)
        if check_winner(board,player):
            return

def check_winner(board):
    draw_counter = 0
    diagonalL = []
    diagonalR = []
    l = 0
    r = 2
    board_transposed = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    for i,k in zip(board,board_transposed):
        if i[l]: diagonalL.append(i[l])
        if i[r]: diagonalR.append(i[r])
        l +=1
        r -=1
        if i[0] != None and i.count(i[0]) == 3 :
            #print('Player ' +i[0] + ' wins')
            return i[0]
        elif k[0] != None and k.count(k[0]) == 3 :
            #print('Player ' +k[0] + ' wins')
            return k[0]

        if None not in i:
            draw_counter+=1

    if (len(diagonalL) == 3 and  diagonalL.count(diagonalL[0]) == 3):
            #print('Player ' + diagonal[0][1] + ' wins')
            return diagonalL[0]
    elif (len(diagonalR) == 3 and diagonalR.count(diagonalR[0]) == 3):
            #print('Player ' + diagonal[0][1] + ' wins')
            return diagonalR[0]


    if draw_counter == 3:
        #print('Draw')
        return 'Draw'

def random_ai(board,player_token):
    x = random.randint(0,2)
    y = random.randint(0,2)
    player_move = (x,y)
    if is_legal_move(board,player_move):
        board[y][x] = player_token
        return board
    else:
        return random_ai(board,player_token)


if __name__ == '__main__':
    game_loop()




