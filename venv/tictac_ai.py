from tictac_main import new_board, render, get_move, is_legal_move, make_move, check_winner, random_ai

def game_loop_ai():
    board = new_board()
    move_count = 0
    players = {1:'X', -1:'O'}
    player_key = 1
    render(board)
    while True:
        player = players[player_key]
        random_ai(board,player)
        render(board)
        move_count+=1
        player_key *= -1
        if check_winner(board, move_count):
            return


if __name__ == '__main__':
    game_loop_ai()