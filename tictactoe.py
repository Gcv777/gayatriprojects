import tkinter as tk
from tkinter import messagebox

# Set up window
root = tk.Tk()
root.title("Tic Tac Toe - X and 0")
root.geometry("320x350")

current_player = "X"  # Start with X
board = ['' for _ in range(9)]
buttons = []

# Function to handle a cell click
def click_cell(index):
    global current_player

    if board[index] == '':
        board[index] = current_player
        buttons[index]['text'] = current_player
        buttons[index]['state'] = 'disabled'

        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins! 🎉")
            reset_game()
        elif '' not in board:
            messagebox.showinfo("Game Over", "It's a draw! 🤝")
            reset_game()
        else:
            current_player = "0" if current_player == "X" else "X"

# Function to check if someone has won
def check_winner(player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to reset the game
def reset_game():
    global board, current_player
    board = ['' for _ in range(9)]
    current_player = "X"
    for btn in buttons:
        btn.config(text='', state='normal')

# Create the grid buttons
for i in range(9):
    btn = tk.Button(root, text='', font=('Arial', 24), width=5, height=2,
                    command=lambda i=i: click_cell(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Start the game window
root.mainloop()
