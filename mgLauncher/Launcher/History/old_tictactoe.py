import tkinter as tk
import tkinter.messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.board = [" "]*9
        self.current_player = "X"
        
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=('Arial', 30), width=6, height=3,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
                
        self.reset_button = tk.Button(self.root, text="Neustart", font=('Arial', 14),
                                       command=self.reset_game)
        self.reset_button.grid(row=3, columnspan=3, pady=10)
        
    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                tkinter.messagebox.showinfo("Tic Tac Toe", f"Spieler {self.current_player} hat gewonnen!")
                self.reset_game()
            elif " " not in self.board:
                tkinter.messagebox.showinfo("Tic Tac Toe", "Unentschieden!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_move()
    
    def computer_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell == " "]
        if empty_cells:
            index = random.choice(empty_cells)
            self.make_move(index // 3, index % 3)
    
    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return True
        return False
    
    def reset_game(self):
        self.board = [" "]*9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ")
            

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
