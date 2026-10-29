# Tic-Tac-Toe with Minimax AI
# Human Player: X
# Computer Player: O

# Create an empty board with 9 positions
board = [" "] * 9


# Display the board
def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


# Check whether a player has won
def check_winner(player):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for positions in winning_positions:
        if all(board[i] == player for i in positions):
            return True

    return False


# Check whether the board is full
def is_draw():
    return " " not in board


# Minimax algorithm
def minimax(depth, is_maximizing):
    # If the computer wins, return a positive score
    if check_winner("O"):
        return 10 - depth

    # If the human wins, return a negative score
    if check_winner("X"):
        return depth - 10

    # If nobody wins and the board is full, it is a draw
    if is_draw():
        return 0

    # Computer's turn: try to get the highest score
    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(depth + 1, False)

                # Undo the move after checking it
                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    # Human's turn: assume the human chooses the best move
    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(depth + 1, True)

                # Undo the move after checking it
                board[i] = " "

                best_score = min(best_score, score)

        return best_score


# Find the best move for the computer
def computer_move():
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            # Try placing the computer's mark
            board[i] = "O"

            # Predict the result using Minimax
            score = minimax(0, False)

            # Undo the trial move
            board[i] = " "

            # Keep the move with the highest score
            if score > best_score:
                best_score = score
                best_move = i

    # Make the best move
    if best_move is not None:
        board[best_move] = "O"
        print("Computer chose position", best_move + 1)


# Main game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the computer is O.")
    print("\nChoose a position from 1 to 9:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    # Continue until someone wins or the game draws
    while True:
        display_board()

        # Get the human player's move
        try:
            position = int(input("Enter your position (1-9): "))

            if position < 1 or position > 9:
                print("Invalid position! Choose 1 to 9.")
                continue

            # Convert position number to a board index
            position = position - 1

            if board[position] != " ":
                print("That position is occupied. Try again.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        # Place the human player's mark
        board[position] = "X"

        # Check whether the human wins
        if check_winner("X"):
            display_board()
            print("Congratulations! You win!")
            break

        # Check for a draw
        if is_draw():
            display_board()
            print("It's a draw!")
            break

        # Let the computer choose using Minimax
        computer_move()
        display_board()

        # Check whether the computer wins
        if check_winner("O"):
            print("Computer wins! Better luck next time.")
            break

        # Check for a draw
        if is_draw():
            print("It's a draw!")
            break

    print("Game over!")


# Start the game
play_game()
