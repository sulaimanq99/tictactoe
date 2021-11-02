

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













if __name__ == '__main__':
    a = new_board()
    render(a)
    b = get_move()
    print(b)