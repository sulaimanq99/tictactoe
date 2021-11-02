

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
    if not board[y][x]:
        board[y][x] = player_token
    else:
        print(str(player_move) + ' is already taken, please try again')
        player_move = get_move(player_token)
        return make_move(board,player_move,player_token)
    return board

def game_loop():
    board = new_board()
    move_count = 0
    players = {1:'X', -1:'O'}
    player_key = 1
    while True:
        render(board)
        player = players[player_key]
        move = get_move(player)
        new = make_move(board, move, player)
        render(new)
        move_count+=1
        player_key *= -1
        #check_winner(board, move_count)
        if check_winner(board, move_count):
            return

def check_winner(board, move_count):
    diagonal = [[],[]]
    l = 0
    r = 2
    board_transposed = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    for i,k in zip(board,board_transposed):
        if i[l]: diagonal[0].append(i[l])
        if i[r]: diagonal[1].append(i[r])
        l +=1
        r -=1
        if i[0] != None and i.count(i[0]) == 3 :
            print('Player ' +i[0] + ' wins')
            return True
        elif k[0] != None and k.count(k[0]) == 3 :
            print('Player ' +k[0] + ' wins')
            return True

    if (len(diagonal[0]) == 3 and  diagonal[0].count(diagonal[0][0]) == 3):
            print('Player ' + diagonal[0][1] + ' wins')
            return True
    elif (len(diagonal[1]) == 3 and diagonal[1].count(diagonal[1][0]) == 3):
            print('Player ' + diagonal[0][1] + ' wins')
            return True


    if move_count == 9:
        print('Draw')
        return True


if __name__ == '__main__':
    game_loop()

