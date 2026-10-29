# Tic-Tac-Toe with Minimax AI

## Project Title

Tic-Tac-Toe Game with Artificial Intelligence

## Description

This project is a simple Tic-Tac-Toe game developed using Python. The human player plays as **X**, while the computer plays as **O**.

The computer uses the **Minimax algorithm** to evaluate possible moves and choose the best available move. The game continues until the human wins, the computer wins, or the board is full and the game ends in a draw.

## Technologies Used

- Python 3
- Functions
- Lists
- Loops and conditional statements
- Minimax algorithm

## Features

- Human versus computer gameplay.
- Computer opponent powered by the Minimax algorithm.
- Clear display of the game board after moves.
- Detection of winning combinations and draws.
- Input validation for invalid numbers and occupied positions.
- Beginner-friendly code with comments explaining the logic.

## How the Minimax Algorithm Works

The Minimax algorithm helps the computer choose its moves by exploring possible future moves.

- The computer tries to maximize its score.
- The human player is assumed to choose moves that minimize the computer's score.
- Winning moves receive positive scores for the computer.
- Human winning moves receive negative scores.
- Draws receive a score of zero.

By comparing these scores, the computer selects the move with the highest score.

## Setup Instructions

### Requirements

- Python 3 installed on your computer, or a Google Colab account.

### How to Run

1. Clone or download this repository.
2. Open the project folder.
3. Run the Python file using the following command:

   `python tic_tac_toe.py`

Alternatively, upload the Python file to Google Colab and run the code in a cell.

## How to Play

1. Run the program.
2. You play as X, and the computer plays as O.
3. Choose a position by entering a number from 1 to 9.
4. The computer automatically makes its move.
5. Continue playing until someone wins or the game ends in a draw.

## GitHub Repository Link

https://github.com/Onima0015/tic-tac-toe-ai
