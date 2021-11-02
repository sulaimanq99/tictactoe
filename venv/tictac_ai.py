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

def get_legal_moves(board):
    moves =[]
    for i in range(3):
        for k in range(3):
            if board[i][k] == None:
                moves.append((k,i))

    return moves

def opp(player):
    if player == 'X': return 'O'
    if player == 'O': return 'X'

def fresh_board(board):
    fresh = [b[:] for b in board]
    return fresh

def minmax(board,player,player_moved):
    scores = []
    winner = check_winner(board)
    if winner == player:
        return 10
    elif winner == 'Draw':
        return 0
    elif winner == opp(player):
        return -10

    moves = get_legal_moves(board)
    for move in moves:
        _board = fresh_board(board)
        make_move(_board,move,player_moved)
        player_moved = opp(player_moved)
        score = minmax(_board,player,player_moved)
        player_moved = opp(player_moved)
        scores.append(score)

    if player == player_moved:
        return max(scores)
    elif player != player_moved:
        return min(scores)

def minmax_ai(board,player):
    best_move = None
    best_score = None
    moves = get_legal_moves(board)
    for move in moves:
        _board = fresh_board(board)
        make_move(_board,move,player)
        player_moved = opp(player)
        score = minmax(_board,player,player_moved)

        if best_score is None or score > best_score:
            best_move = move
            best_score = score

    return make_move(board,best_move,player)


def human_player(board,player_token):
    move = get_move(player_token)
    board = make_move(board, move, player_token)

def end_game(outcome):
    if outcome != 'Draw':
        print(f'Player {outcome} wins the game')
    else:
        print('Draw')

def game_loop_ai():
    board = new_board()
    players = {1:'X', -1:'O'}
    player_key = 1
    render(board)
    while True:
        player = players[player_key]
        human_player(board,player)
        render(board)
        player_key *= -1
        if check_winner(board):
            end_game(check_winner(board))
            return
        player = players[player_key]
        minmax_ai(board,player)
        render(board)
        player_key *= -1
        if check_winner(board):
            end_game(check_winner(board))
            return


if __name__ == '__main__':
    board = [
        ['X', 'O', 'O'],
        [None, None, None],
        [None, None, 'X']
    ]

    a = minmax_ai(board,'O')
    render(a)

    game_loop_ai()