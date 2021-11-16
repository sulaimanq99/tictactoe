# tictactoe
Tic tac toe game. Can either play with 2 players, against the computer or run the computer against it self. Three algorithms.

1)Computer will randomly choose a valid place

2)Computer will check if a move will win them the game and do that. Otherwise will check if the opponent is one move away from winning and block them. Otherwise defaults to random

3)Makes use of the min max algorithm, programmed recursively. Assumes the player will always make the optimal move, so can potentially be beat this way. Speed can be improved by caching as due to recursion it is quite slow


