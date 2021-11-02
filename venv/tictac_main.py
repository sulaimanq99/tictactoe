

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














if __name__ == '__main__':
    a = new_board()
    render(a)