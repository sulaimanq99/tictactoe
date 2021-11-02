

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

def get_move():
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
        player_move = get_move()
        return make_move(board,player_move,player_token)
    return board












if __name__ == '__main__':
    board = new_board()
    render(board)
    move = get_move()
    new = make_move(board,move,'X')
    render(new)
    move = get_move()
    new = make_move(board,move,'O')
    render(new)