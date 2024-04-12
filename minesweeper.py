from tkinter import *
from tkinter.scrolledtext import ScrolledText
import random

score_value = 0

def create_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def plant_mines(grid, num_mines):
    rows = len(grid)
    cols = len(grid[0])
    mines_planted = 0
    while mines_planted < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if grid[row][col] != -1:
            grid[row][col] = -1
            mines_planted += 1

def count_adjacent_mines(grid, row, col):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if grid[i][j] == -1:
                count += 1
    return count

def left_click(row, col):
    global score_value
    if minefield[row][col] == -1:
        buttons[row][col].config(text="0", state=DISABLED)
        
        for r in range(10):
            for c in range(10):
                buttons[r][c].config(state=DISABLED)
        restart_button.pack(side=TOP, pady=10)
    else:
        adjacent_mines = count_adjacent_mines(minefield, row, col)
        buttons[row][col].config(text="1", state=DISABLED)
        score_value += 1
        score.delete(1.0, END)
        score.insert(END, str(score_value) + " ")

def restart_game():
    global minefield, score_value
    for row in range(10):
        for col in range(10):
            buttons[row][col].config(text="", state=NORMAL)
    minefield = create_grid(10, 10)
    plant_mines(minefield, 10)
    score_value = 0
    score.delete(1.0, END)

game = Tk()

WIDTH = 310
HEIGHT = 400

game.geometry(f"{WIDTH}x{HEIGHT}")
game.title("Minesweeper")

game.resizable(False, False)

score_frame = Frame(game, height=50)
score_frame.pack(side=TOP, fill=X, expand=True, padx=5)
score_frame.pack_propagate(False)

score_placeholder = LabelFrame(score_frame, width=80, text="Puntaje")
score_placeholder.pack(side=LEFT, fill=Y)
score_placeholder.pack_propagate(False)

score = Text(score_placeholder, font=("",19))
score.pack(side=LEFT, fill=BOTH, expand=True)

game_frame = Frame(game, height=300, bg="blue")
game_frame.pack(side=TOP, fill=X, expand=True)
game_frame.pack_propagate(False)

minefield = create_grid(10, 10)
plant_mines(minefield, 10)

buttons = []
for row in range(10):
    button_row = []
    for col in range(10):
        cell = Button(game_frame, width=3, height=1, command=lambda r=row, c=col: left_click(r, c))
        cell.grid(row=row, column=col)
        button_row.append(cell)
    buttons.append(button_row)

restart_button = Button(score_frame, text="Reiniciar", command=restart_game)

game.mainloop()