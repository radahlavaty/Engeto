"""
project_2.py: second Engeto Online Python Academy project
author: Radek Hlavatý
email: rada.hlavaty@gmail.com
discord: radhead#2491
"""
#Import
import time
import datetime
import os
import random

from template import header

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def display_header():
    """Displays the game's header and rules."""
    print(header)

def initialize_board():
    """Creates and returns a 3x3 game board (list of lists) initialized with spaces."""
    board = []
    for _ in range(3):
        board.append([' ',' ',' '])
    return board

def print_board(board):
    """Prints the current state of the board."""
    print(40 * "-")
    for row in board:
        print("+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+")
    print(40 * "=")

def choose_player_type():
    """Lets the user choose the type of opponent: another player or the computer."""
    while True:
        player_type = input("Play against another player (1) or the computer (2)? Enter 1 or 2: ").strip()
        if player_type in ['1', '2']:
            return player_type
        else:
            print("Invalid input. Please enter 1 or 2.")

def get_player_move(player):
    """Prompts the player for a move, validates it, and returns (row, col)."""
    while True:
        move_input = input(f"Player {player} | Please enter your move number (1-9): ")
        if move_input.isdigit():  # Check if the input is a digit
            move = int(move_input) - 1  # Convert to int and adjust for zero-based indexing
            if 0 <= move <= 8:
                # Map the move to its corresponding row and column
                move_to_coordinations = {
                    0: (0, 0), 
                    1: (0, 1), 
                    2: (0, 2),
                    3: (1, 0), 
                    4: (1, 1), 
                    5: (1, 2),
                    6: (2, 0), 
                    7: (2, 1), 
                    8: (2, 2)
                }
                return move_to_coordinations[move]
            else:
                print("Invalid move. Please try again.")
        else:
            print("Please enter a number.")

def make_move(board, row, col, player):
    """Places the player's move on the board if the space is not already taken."""
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    print("This position is already taken. Please choose another.")
    return False

def computer_move(board, player):
    """Computer selects a free spot randomly with a human-like delay."""
    print(f"Computer ({player}) is thinking...")
    time.sleep(random.randint(1, 3))  # Simulate thinking with a 1 to 3 seconds delay
    
    free_spots = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                free_spots.append((row, col))

    if free_spots:
        row, col = random.choice(free_spots)
        board[row][col] = player
        return True
    return False

def check_winner(board, player):
    """Checks if the player has won the game."""
    for i in range(3):
        # Check each row for a win
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        # Check each column for a win
        elif board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    
    # Check diagonal (top-left to bottom-right) for a win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    # Check diagonal (top-right to bottom-left) for a win
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    # If none of the conditions are met, return False
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                # If any cell is empty, the game is not a draw
                return False
    # If all cells are filled and no winner, it's a draw
    return True

def switch_player(player):
    """Switches the current player."""
    if player == 'X':
        return 'O'
    else:
        return 'X'  

def ask_for_new_game():
    """Prompts the user to decide if they want to start a new game."""
    while True:
        response = input("Do you want to play again? (yes/no): ").lower()
        if response == 'yes':
            return True
        elif response == 'no':
            return False
        else:
            print("Invalid response. Please answer 'yes' or 'no'.")

def clear_screen():
    """Clears the terminal screen."""
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/Mac
    else:
        os.system('clear')

def tic_tac_toe_game():
    """Runs the main game loop with an option to replay the game."""
    play_again = True

    while play_again:
        clear_screen()
        display_header()
        
        player_type = choose_player_type()

        board = initialize_board()
        current_player = 'X'
        game_winner = None  # Variable to store the winner
        start_time = time.time()
        start_datetime = datetime.datetime.now()  # Record start datetime

        while True:
            print_board(board)
            if current_player == 'O' and player_type == '2':
                # If the current player is O and the player chose to play against the computer
                computer_move(board, current_player)
                print(f"Computer ({current_player}) made its move.")
            else:
                while True:
                    row, col = get_player_move(current_player)
                    if make_move(board, row, col, current_player):
                        break
            
            if check_winner(board, current_player):
                print_board(board)             
                if current_player == 'X' or player_type == '1':
                    game_winner = current_player + ' (Human)'  
                else:
                    game_winner = 'O' + ' (Computer)'
                print(f"Congratulations, Player {game_winner} wins!")
                break
            
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                game_winner = 'Draw'
                break
            current_player = switch_player(current_player)
        
        end_time = time.time()
        end_datetime = datetime.datetime.now()
        duration = end_time - start_time
        print(f"Game duration: {duration:.2f} seconds.")
        
        # Format start and end datetime
        start_str = start_datetime.strftime("%Y-%m-%d %H:%M:%S")
        end_str = end_datetime.strftime("%Y-%m-%d %H:%M:%S")

        # Write game results with date and time to file
        with open("tic_tac_toe_results.txt", "a") as file:
            file.write(f"Date: {start_datetime.date()}, Start: {start_str}, End: {end_str}, "
                       f"Game Duration: {duration:.2f} seconds, Winner: {game_winner}\n")

        play_again = ask_for_new_game()

if __name__ == "__main__":
    tic_tac_toe_game()
