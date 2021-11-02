from tictac_main import new_board, render, get_move, is_legal_move, make_move, check_winner, random_ai

def next_move_winner(board,player):
    board_transposed = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    diagonalL, diagonalR = [], []
    l, r = 0, 2
    for i in range(3):
        if board[i].count(player) == 2 and None in board[i]:
            x = board[i].index(None)
            return (i, x)
        elif board_transposed[i].count(player) == 2 and None in board_transposed[i]:
            x = board_transposed[i].index(None)
            return(x, i)
        diagonalL.append(board[i][l])
        diagonalR.append(board[i][r])
        l += 1
        r -= 1
        if diagonalL.count(player) == 2 and None in diagonalL:
            x = diagonalL.index(None)
            return(x, x)
        elif diagonalR.count(player) == 2 and None in diagonalR:
            x = diagonalR.index(None)
            if x == 0:
                return(0, 2)
            elif x == 1:
                return(x, x)
            elif x == 2:
                return(2, 0)
    return False


def finds_winning_moves_ai(board, player):
    next_move = next_move_winner(board,player)
    if next_move != False:
        y = next_move[0]
        x = next_move[1]
        board[y][x] = player
        return board
    else:
        return random_ai(board,player)

def finds_winning_and_losing_moves_ai(board, player,player_key):
    players = {1: 'X', -1: 'O'}
    next_move = next_move_winner(board, player)
    if next_move != False:
        y = next_move[0]
        x = next_move[1]
        board[y][x] = player
        return board

    block = players[player_key*-1]
    next_move = next_move_winner(board, block)
    if next_move != False:
        y = next_move[0]
        x = next_move[1]
        board[y][x] = player
        return board
    return random_ai(board,player)





def game_loop_ai():
    board = new_board()
    move_count = 0
    players = {1:'X', -1:'O'}
    player_key = 1
    render(board)
    while True:
        player = players[player_key]
        finds_winning_and_losing_moves_ai(board,player,player_key)
        render(board)
        move_count+=1
        player_key *= -1
        if check_winner(board, move_count):
            return


if __name__ == '__main__':
    '''
    board = [
        ['X', 'X', None],
        [None, 'O', None],
        ['O', None, None]
    ]
    finds_winning_moves_ai(board, 'X')
    finds_winning_moves_ai(board, 'X')
    # => should always print (1, 0)

    finds_winning_moves_ai(board, 'O')
    finds_winning_moves_ai(board, 'O')
    # => should always print (2, 1)'''




    game_loop_ai()