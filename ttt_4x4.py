import random

# Function to create an empty 4x4 board
def create_board():
    return [[' ' for _ in range(4)] for _ in range(4)]

# Function to display the board in the console
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 9)

# Function to check if a move is valid
def is_valid_move(board, row, col):
    return board[row][col] == ' '

# Function to check for a winner
def is_winner(board, player):
    for i in range(4):
        if all(board[i][j] == player for j in range(4)) or all(board[j][i] == player for j in range(4)):
            return True

    if all(board[i][i] == player for i in range(4)) or all(board[i][3 - i] == player for i in range(4)):
        return True

    return False

# Function to check for a tie
def is_tie(board):
    return all(board[i][j] != ' ' for i in range(4) for j in range(4))

# Minimax algorithm
def minimax(board, depth, player):
    if player == 'X':
        best_move = [-1, -1, -float('inf')]
    else:
        best_move = [-1, -1, float('inf')]

    if depth == 0 or is_winner(board, 'X') or is_winner(board, 'O') or is_tie(board):
        score = 0
        if is_winner(board, 'X'):
            score = 1
        elif is_winner(board, 'O'):
            score = -1
        return [-1, -1, score]

    for i in range(4):
        for j in range(4):
            if board[i][j] == ' ':
                board[i][j] = player
                score = minimax(board, depth - 1, 'O' if player == 'X' else 'X')
                board[i][j] = ' '
                score[0], score[1] = i, j

                if player == 'X':
                    if score[2] > best_move[2]:
                        best_move = score
                else:
                    if score[2] < best_move[2]:
                        best_move = score

    return best_move

# Main game function
def game():
    board = create_board()
    player_turn = True
    game_active = True

    print("Welcome to the 4x4 Tic-Tac-Toe game!")

    while game_active:
        display_board(board)

        if player_turn:
            row = int(input("Choose a row (1-4): ")) - 1
            col = int(input("Choose a column (1-4): ")) - 1
        else:
            print("Computer's turn...")
            computer_move = minimax(board, 4, 'X')
            row, col = computer_move[0], computer_move[1]

        if is_valid_move(board, row, col):
            player = 'X' if player_turn else 'O'
            board[row][col] = player

            if is_winner(board, player):
                display_board(board)
                print(f"{player} wins!")
                game_active = False
            elif is_tie(board):
                display_board(board)
                print("It's a tie!")
                game_active = False
            else:
                player_turn = not player_turn
        else:
            print("Invalid move. Please try again.")

    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() == "yes":
        game()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    game()
