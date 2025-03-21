import random

def initialize_board():
    return [[1,2,3],[4,5,6],[7,8,9]]

def print_current_board(board):
    for row in board:
        print(row)
    print()

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

# returns position of win if possible, False if not
def win_possible(board, letter: str):
    other_letter = ''
    if letter == 'X':
        other_letter = 'O'
    else:
        other_letter = 'X'

    # horizontal
    for row in board:
        if row.count(letter) == 2 and row.count(other_letter) == 0:
            for i in row:
                if type(i) is int:
                    return i
    # vertical
    for j in range(len(board)):
        col = []
        for i in range(len(board)):
            col.append(board[i][j])
        if col.count(letter) == 2 and col.count(other_letter) == 0:
            for i in col:
                if type(i) is int:
                    return i

    # diagonal up -> down
    diag = []
    for i in range(len(board)):
        diag.append(board[i][i])
    if diag.count(letter) == 2 and diag.count(other_letter) == 0:
            for i in diag:
                if type(i) is int:
                    return i

    # diagonal down -> up
    diag = []
    for i in range(len(board)):
        diag.append(board[i][len(board) - 1 - i])
    if diag.count(letter) == 2 and diag.count(other_letter) == 0:
            for i in diag:
                if type(i) is int:
                    return i
    return False

# returns position of block if possible, False if not
def block_possible(board, letter_of_current_player: str):
    other_letter = ''
    if letter_of_current_player == 'X':
        other_letter = 'O'
    else:
        other_letter = 'X'

    # horizontal
    for row in board:
        if row.count(other_letter) == 2 and row.count(letter_of_current_player) == 0:
            for i in row:
                if type(i) is int:
                    return i
    # vertical
    for j in range(len(board)):
        col = []
        for i in range(len(board)):
            col.append(board[i][j])
        if col.count(other_letter) == 2 and col.count(letter_of_current_player) == 0:
            for i in col:
                if type(i) is int:
                    return i

    # diagonal up -> down
    diag = []
    for i in range(len(board)):
        diag.append(board[i][i])
    if diag.count(other_letter) == 2 and diag.count(letter_of_current_player) == 0:
            for i in diag:
                if type(i) is int:
                    return i

    # diagonal down -> up
    diag = []
    for i in range(len(board)):
        diag.append(board[i][len(board) - 1 - i])
    if diag.count(other_letter) == 2 and diag.count(letter_of_current_player) == 0:
            for i in diag:
                if type(i) is int:
                    return i
    return False

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

def is_cat_game(board, human_in_game: bool):
    chars_in_game = []
    for row in board:
        for j in row:
            chars_in_game.append(j)
    if len(set(chars_in_game)) == 2:
        if human_in_game:
            cat = r"""
            /\_/\   
            ( o.o )  
            > ^ >===========o  
                ||     ||
                ||     ||
                ~~     ~~
            """
            print(cat)
        return True
    else:
        return False

def initialize_spots_remaining():
    my_set = set()
    for i in range(1, 10):
        my_set.add(i)
    return my_set

def updateWin(map: dict, letter: str, moveCombination: tuple):
    """
    Update win results for a specific 2 opening move combination.
    """
    result_dict = map.get(moveCombination)
    letter_win_str = f'{letter}win'
    result_dict.update({letter_win_str: result_dict.get(letter_win_str) + 1})

def tictactoe_pvp():
    board = initialize_board()
    spots_remaining = initialize_spots_remaining()
    print_current_board(board)
    
    game_over = False
    turn_counter = 1
    while (game_over is False):
        # odds are X's turns
        if turn_counter % 2 == 1:
            letter = 'X'
            x_pos = int(input('What position would X like to place?\n'))
            if x_pos in spots_remaining:
                spots_remaining.remove(x_pos)
                redraw_position(x_pos, letter, board)
                if check_for_winner(board, letter) is True:
                    print(f'Congratulations, {letter} wins!')
                    game_over = True
                elif is_cat_game(board, True) is True:
                    print('Tie! No winner today.')
                    game_over = True
                else:
                    turn_counter += 1
            else:
                print('Try again. Enter valid position.')
                print(f'Valid Positions: {spots_remaining}')
        # evens are O's turns
        else:
            letter = 'O'
            y_pos = int(input('What position would O like to place?\n'))
            if y_pos in spots_remaining:
                spots_remaining.remove(y_pos)
                redraw_position(y_pos, letter, board)
                if check_for_winner(board, letter) is True:
                    print(f'Congratulations, {letter} wins!')
                    game_over = True
                elif is_cat_game(board, True) is True:
                    print('Tie! No winner today.')
                    game_over = True
                else:
                    turn_counter += 1
            else:
                print('Try again. Enter valid position.')
                print(f'Valid Positions: {spots_remaining}')
        print_current_board(board)

def tictactoe_pve():
    board = initialize_board()
    spots_remaining = initialize_spots_remaining()
    print_current_board(board)
    game_over = False

    turn_counter = random.randint(0, 1)
    if turn_counter == 1:
        print('You won the coin flip! You go first.')
    else:
        print('Computer goes first.')

    while (game_over is False):
        # odds are X's turns (HUMAN)
        if turn_counter % 2 == 1:
            letter = 'X'
            x_pos = int(input('What position would X like to place?\n'))
            if x_pos in spots_remaining:
                spots_remaining.remove(x_pos)
                redraw_position(x_pos, letter, board)
                if check_for_winner(board, letter) is True:
                    print(f'Congratulations, {letter} wins!')
                    game_over = True
                elif is_cat_game(board, True) is True:
                    print('Tie! No winner today.')
                    game_over = True
                else:
                    turn_counter += 1
            else:
                print('Try again. Enter valid position.')
                print(f'Valid Positions: {spots_remaining}')
        # evens are O's turns (COMPUTER)
        else:
            letter = 'O'
            y_pos = random.sample(population=list(spots_remaining), k=1)[0]
            spots_remaining.remove(y_pos)
            print(f'Computer plays position {y_pos}')

            redraw_position(y_pos, letter, board)
            if check_for_winner(board, letter) is True:
                print(f'Congratulations, {letter} wins!')
                game_over = True
            elif is_cat_game(board, True) is True:
                print('Tie! No winner today.')
                game_over = True
            else:
                turn_counter += 1
        print_current_board(board)

# returns ((move1, move2), winner)
def tictactoe_com_com():
    board = initialize_board()
    spots_remaining = initialize_spots_remaining()
    
    winner = None
    game_over = False
    turn_counter = 1
    first_2_moves = []
    while (game_over is False):
        # odds are X's turns
        if turn_counter % 2 == 1:
            letter = 'X'
            x_pos = random.sample(population=list(spots_remaining), k=1)[0]
            spots_remaining.remove(x_pos)

            if turn_counter <= 2:
                first_2_moves.append(x_pos)

            redraw_position(x_pos, letter, board)
            if check_for_winner(board, letter) is True:
                winner = letter
                # print(f'Congratulations, {letter} wins!')
                # input('Holdup partner X WINS')
                game_over = True
            elif is_cat_game(board, False) is True:
                winner = 'CAT'
                # print('Tie! No winner today.')
                game_over = True
            else:
                turn_counter += 1
        # evens are O's turns
        else:
            letter = 'O'
            y_pos = random.sample(population=list(spots_remaining), k=1)[0]
            spots_remaining.remove(y_pos)

            if turn_counter <= 2:
                first_2_moves.append(y_pos)

            redraw_position(y_pos, letter, board)
            if check_for_winner(board, letter) is True:
                winner = letter
                # print(f'Congratulations, {letter} wins!')
                # input('Holdup partner O WINS')
                game_over = True
            elif is_cat_game(board, False) is True:
                winner = 'CAT'
                # print('Tie! No winner today.')
                game_over = True
            else:
                turn_counter += 1
        # print_current_board(board)

    return_tuple = (tuple(first_2_moves), winner)
    return return_tuple

def tictactoe_smart(best_response: dict):
    board = initialize_board()
    spots_remaining = initialize_spots_remaining()
    # print_current_board(board)
    winner = ''
    game_over = False

    turn_counter = 1
    opening_move = 0
    while game_over is False:
        # odds are X's turns (HUMAN)
        if turn_counter % 2 == 1:
            letter = 'X'
            x_pos = random.sample(population=list(spots_remaining), k=1)[0]
            if x_pos in spots_remaining:
                if turn_counter == 1:
                    opening_move = x_pos

                spots_remaining.remove(x_pos)
                # print(f'Dumb Computer plays position {x_pos}')
                redraw_position(x_pos, letter, board)
                if check_for_winner(board, letter) is True:
                    # print(f'Congratulations, {letter} wins!')
                    winner = letter
                    game_over = True
                elif is_cat_game(board, False) is True:
                    # print('Tie! No winner today.')
                    winner = 'CAT'
                    game_over = True
                else:
                    turn_counter += 1
            else:
                print('Try again. Enter valid position.')
                print(f'Valid Positions: {spots_remaining}')
        # evens are O's turns (COMPUTER)
        else:
            letter = 'O'

            if turn_counter == 2:
                y_pos = best_response.get(opening_move)
            else:
                win_pos = win_possible(board, letter)
                block_pos = block_possible(board, letter)
                if win_pos:
                    y_pos = win_pos
                elif block_pos:
                    y_pos = block_pos
                else:
                    y_pos = random.sample(population=list(spots_remaining), k=1)[0]
            spots_remaining.remove(y_pos)
            # print(f'Smart Computer plays position {y_pos}')

            redraw_position(y_pos, letter, board)
            if check_for_winner(board, letter) is True:
                # print(f'Congratulations, {letter} wins!')
                winner = letter
                game_over = True
            elif is_cat_game(board, False) is True:
                # print('Tie! No winner today.')
                winner = 'CAT'
                game_over = True
            else:
                turn_counter += 1
        # print_current_board(board)
    return winner

# {(move1, move2) -> {'Xwins': n, 'Owins':m}}
def print_move_results(move_results: dict):
    for combination in move_results:
        wl_record = move_results.get(combination)
        print(f'{combination} -> {wl_record}')

# returns: {opening move -> best response move}
def get_best_moves_for_player2(move_results: dict):
    best_response_to_opener_dict = dict()
    # loop through all possible openers
    for opener in range(1,10):
        best_response = 0
        best_response_winrate = 0
        # loop through all responses to opener
        for response in range(1,10):
            if opener != response:
                num_Xwin = move_results.get((opener, response)).get('Xwin')
                num_Owin = move_results.get((opener, response)).get('Owin')
                cur_winrate = num_Xwin / num_Owin
                if cur_winrate > best_response_winrate:
                    best_response = response
                    best_response_winrate = cur_winrate
        best_response_to_opener_dict.update({opener: best_response})

    return best_response_to_opener_dict

def menu():
    game_over = False
    move_results = dict()
    while game_over is False:
        art = r"""
        X | O | X  
       ---+---+---  
        O | 💀 | O  
       ---+---+---  
        X | O | X  
        """
        print(art)

        print('Welcome to Tic Tac Toe!')
        result = input('1) Play Human v. Human\n2) Play Human v. Computer.\n3) Simulate Computer v. Computer\n4) Computer v. SMARTCOM \n5) Exit Game\n')
        
        if result == '1':
            tictactoe_pvp()
        elif result == '2':
            tictactoe_pve()
        elif result == '3':
            game_log = [] # list of tuples, [((move1, move2), winner)]

            iterations = 10000
            print(f'Simulating Computer v. Computer {iterations} times...')
            loading_num = int(iterations / 10)
            percent_complete = 10
            for i in range(1, iterations + 1):
                game_result = tictactoe_com_com()
                game_log.append(game_result)
                move_combination = game_result[0]
                letter_winner = game_result[1]
                
                if move_combination in move_results and ((letter_winner == 'X') or (letter_winner == 'O')):
                    updateWin(map=move_results, letter=letter_winner, moveCombination=move_combination)
                else:
                    if letter_winner == 'X':
                        move_results.update({move_combination: {'Xwin': 1, 'Owin': 0}})
                    elif letter_winner == 'O':
                        move_results.update({move_combination: {'Xwin': 0, 'Owin': 1}})

                if i == loading_num:
                    print(f'Done with {percent_complete}% of iterations...')
                    percent_complete += 10
                    loading_num += int(iterations/10)

            num_X_wins = 0
            num_O_wins = 0
            num_cat_games = 0

            for tup in game_log:
                if tup[1] == 'X':
                    num_X_wins += 1
                elif tup[1] == 'O':
                    num_O_wins += 1
                else:
                    num_cat_games += 1

            print(f'\nX / Player 1 Wins: {num_X_wins}')
            print(f'O / Player 2 Wins: {num_O_wins}')
            print(f'Cat Games: {num_cat_games}')
            print(f'X / Player 1 Win Probability: {num_X_wins / (num_X_wins + num_O_wins + num_cat_games)}')
            print(f'O / Player 2 Win Probability: {num_O_wins / (num_X_wins + num_O_wins + num_cat_games)}')
            print(f'Cat Game Probability: {num_cat_games / (num_X_wins + num_O_wins + num_cat_games)}\n')
            # Print All Combos and Win Record
            print(f'Number of Combinations: {len(move_results)}')
            print_move_results(move_results)

        elif result == '4':
            if len(move_results) == 0:
                print('Run Computer v. Computer before running TicTacToe v. Smart Bot')
            else:
                best_moves_for_player2 = get_best_moves_for_player2(move_results)
                # print(best_moves_for_player2)
                game_log = []
                iterations = 10000
                print(f'Simulating Dumb Computer v. Smart Computer {iterations} times...')
                for i in range(iterations):
                    game_log.append(tictactoe_smart(best_moves_for_player2))
                
                # Print number of X/O/Cat and Probabilities
                num_X_wins = 0
                num_O_wins = 0
                num_cat_games = 0
                for winner in game_log:
                    if winner == 'X':
                        num_X_wins += 1
                    elif winner == 'O':
                        num_O_wins += 1
                    else: # cat game
                        num_cat_games += 1
                total_games = num_X_wins + num_O_wins + num_cat_games
                print(f'\nX / Player 1 Wins: {num_X_wins}')
                print(f'O / Player 2 Wins: {num_O_wins}')
                print(f'Cat Games: {num_cat_games}')
                print(f'X / Player 1 Win Probability: {num_X_wins / total_games}')
                print(f'O / Player 2 Win Probability: {num_O_wins / total_games}')
                print(f'Cat Game Probability: {num_cat_games / total_games}\n')

        elif result == '5':
            print('Goodbye :(')
            game_over = True
        else:
            print('Invalid input. >:[')
    print('Thank you for playing TicTacToe.v2 !')

menu()
