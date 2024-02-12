import tkinter as tk
from tkinter import messagebox
import subprocess

class SpieleAuswahlGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Spiele Auswahl")
        self.root.geometry("250x250")

        label = tk.Label(root, text="Wähle ein Spiel:")
        label.pack(pady=10)

        # Buttons for game selection
        self.create_game_button("Quiz", self.quiz_starten)
        self.create_game_button("TicTacToe", self.tictactoe_starten)
        self.create_game_button("Snake", self.snake_starten)
        self.create_game_button("Tetris", self.tetris_starten)
        self.create_game_button("TimeTheFreez", self.TTF_starten)

    def create_game_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command, width=20)
        button.pack(pady=5)

    def quiz_starten(self):
        messagebox.showinfo("Quiz", "Quiz wird gestartet.")
        subprocess.run(["python", "Launcher\Games\quiz\quiz.py"])

    def tictactoe_starten(self):
        messagebox.showinfo("TicTacToe", "TicTacToe wird gestartet.")
        subprocess.run(["python", r"Launcher\Games\tictactoe\tictactoe.py", 'r'])

    def snake_starten(self):
        messagebox.showinfo("Snake", "Snake wird gestartet.")
        subprocess.run(["python", "Launcher\Games\snake\snake.py"])

    def TTF_starten(self):
        messagebox.showinfo("TimeTheFreez", "TimeTheFreez wird gestartet.")
        subprocess.run(["python", "Launcher\Games\TimeTheFreez\main.py"])

    def tetris_starten(self):
        messagebox.showinfo("Tetris", "Tetris wird gestartet.")
        subprocess.run(["python", r"Launcher\Games\tetris\tetris.py",'r'])    

if __name__ == "__main__":
    root = tk.Tk()
    app = SpieleAuswahlGUI(root)
    root.mainloop()


# If you would like to add your own Game, here you got a template for it
# put this code underneath "Buttons for game selection (l.14)" and replace "NAME_OF_YOUR_GAME" with your GameName
# self.create_game_button("NAME_OF_YOUR_GAME", self.NAME_OF_YOUR_GAME_starten)
# add a def for your Game underneath line 39 and replace "NAME_OF_YOUR_GAME" as well as "PATH_TO_YOUR_GAME"
# template:
# def NAME_OF_YOUR_GAME_starten(self):
#       messagebox.showinfo("NAME_OF_YOUR_GAME", "NAME_OF_YOUR_GAME wird gestartet.")
#       subprocess.run(["python", "PATH_TO_YOUR_GAME"])
# Done!