# Initialize the empty Tic-Tac-Toe board as a list of lists
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

# Function to check if a player has won the game
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):   
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full (a tie)
def check_tie(board):
    return all(cell != " " for row in board for cell in row)

# Main game loop
current_player = "X"
while True:
    # Display the current board
    display_board(board)

    # Get the current player's move
    while True:
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            break
        else:
            print("Invalid move. Try again.")

    # Place the current player's symbol on the board
    board[row][col] = current_player

    # Check if the current player has won
    if check_win(board, current_player):
        display_board(board)
        print(f"Player {current_player} wins!")
        break

    # Check for a tie (the board is full)
    if check_tie(board):
        display_board(board)
        print("It's a tie!")
        break

    # Switch to the other player for the next turn
    current_player = "O" if current_player == "X" else "X"
