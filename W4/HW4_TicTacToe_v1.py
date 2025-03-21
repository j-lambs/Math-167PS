import os
import random

def initialize_board():
    return [[1,2,3],[4,5,6],[7,8,9]]

def print_current_board(board):
    for row in board:
        print(row)

def get_elt_value(pos: int, board):
    if pos >= 1 and pos <= 3:
        return board[0][pos - 1]
    if pos >= 4 and pos <= 6:
        return board[1][pos % 3 - 1]
    if pos >= 7 and pos <= 9:
        return board[2][pos % 3 - 1]

def position_is_valid(pos: str, board) -> bool:
    pos = int(pos)
    if (pos >= 1 and pos <= 9) and isinstance(get_elt_value(pos, board), int):
        return True
    return False

def redraw_position(pos: str, letter: str, board):
    pos = int(pos)
    if pos >= 1 and pos <= 3:
        board[0][pos - 1] = letter
    if pos >= 4 and pos <= 6:
        board[1][pos % 3 - 1] = letter
    if pos >= 7 and pos <= 9:
        board[2][pos % 3 - 1] = letter
    return board

def check_for_winner(board, letter: str):
    # horizontal
    for row in board:
        if len(set(row)) == 1:
            return True
    
    # vertical
    for j in range(len(board)):
        col = []
        for i in range(len(board)):
            col.append(board[i][j])
        if len(set(col)) == 1:
            return True

    # diagonal up -> down
    diag = []
    for i in range(len(board)):
        diag.append(board[i][i])
    if len(set(diag)) == 1:
        return True

    # diagonal down -> up
    diag = []
    for i in range(len(board)):
        diag.append(board[i][len(board) - 1 - i])
    if len(set(diag)) == 1:
        return True

    return False

def is_cat_game(board):
    chars_in_game = []
    for row in board:
        for j in row:
            chars_in_game.append(j)
    if len(set(chars_in_game)) == 2:
        return True
    else:
        return False

def tictactoe_pvp():
    board = initialize_board()
    print_current_board(board)
    
    game_over = False
    turn_counter = 1
    while (game_over is False):
        # odds are X's turns
        if turn_counter % 2 == 1:
            letter = 'X'
            x_pos = int(input('What position would X like to place?\n'))
            if position_is_valid(x_pos, board):
                redraw_position(x_pos, letter, board)
                if check_for_winner(board, letter) is True:
                    print(f'Congratulations, {letter} wins!')
                    game_over = True
                elif is_cat_game(board) is True:
                    print('Tie! No winner today.')
                    game_over = True
                else:
                    turn_counter += 1
            else:
                print('Try again. Enter valid position.')
        # evens are O's turns
        else:
            letter = 'O'
            y_pos = input('What position would O like to place?\n')
            if position_is_valid(y_pos, board):
                redraw_position(y_pos, letter, board)
                if check_for_winner(board, letter) is True:
                    print(f'Congratulations, {letter} wins!')
                    game_over = True
                elif is_cat_game(board) is True:
                    print('Tie! No winner today.')
                    game_over = True
                else:
                    turn_counter += 1
            else:
                print('Try again. Enter valid position.')
        print_current_board(board)

def tictactoe_human_com():
    board = initialize_board()
    print_current_board(board)
    
    game_over = False
    turn_counter = 1
    while (game_over is False):
        # odds are X's turns
        if turn_counter % 2 == 1:
            letter = 'X'
            x_pos = int(input('What position would X like to place?\n'))
            if position_is_valid(x_pos, board):
                redraw_position(x_pos, letter, board)
                if check_for_winner(board, letter) is True:
                    print(f'Congratulations, {letter} wins!')
                    game_over = True
                elif is_cat_game(board) is True:
                    print('Tie! No winner today.')
                    game_over = True
                else:
                    turn_counter += 1
            else:
                print('Try again. Enter valid position.')
        # evens are O's turns
        else:
            letter = 'O'
            y_pos = random.randint(1, 9)
            if position_is_valid(y_pos, board):
                redraw_position(y_pos, letter, board)
                if check_for_winner(board, letter) is True:
                    print(f'Congratulations, {letter} wins!')
                    game_over = True
                elif is_cat_game(board) is True:
                    print('Tie! No winner today.')
                    game_over = True
                else:
                    turn_counter += 1
        print_current_board(board)

def tictactoe_com_com():
    board = initialize_board()
    print_current_board(board)
    
    game_over = False
    turn_counter = 1
    while (game_over is False):
        # odds are X's turns
        if turn_counter % 2 == 1:
            letter = 'X'
            x_pos = random.randint(1, 9)
            if position_is_valid(x_pos, board):
                redraw_position(x_pos, letter, board)
                if check_for_winner(board, letter) is True:
                    print(f'Congratulations, {letter} wins!')
                    input('Holdup partner X WINS')
                    game_over = True
                elif is_cat_game(board) is True:
                    print('Tie! No winner today.')
                    game_over = True
                else:
                    turn_counter += 1
        # evens are O's turns
        else:
            letter = 'O'
            y_pos = random.randint(1, 9)
            if position_is_valid(y_pos, board):
                redraw_position(y_pos, letter, board)
                if check_for_winner(board, letter) is True:
                    print(f'Congratulations, {letter} wins!')
                    input('Holdup partner O WINS')
                    game_over = True
                elif is_cat_game(board) is True:
                    print('Tie! No winner today.')
                    game_over = True
                else:
                    turn_counter += 1
        print_current_board(board)

def menu():
    game_over = False
    while game_over is False:
        os.system('clear')
        print('Welcome to Tic Tac Toe!')
        result = input('1) Play Human v. Human\n2) Play Human v. Computer.\n3) Computer v. Computer\n4) Exit Game\n')
        if result == '1':
            tictactoe_pvp()
        elif result == '2':
            tictactoe_human_com()
        elif result == '3':
            tictactoe_com_com()
        elif result == '4':
            print('Goodbye :(')
            game_over = True
        else:
            print('Invalid input. >:[')
    print('Thank you for playing TicTacToe.v1')

menu()
