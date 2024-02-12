import tkinter as tk
from tkinter import messagebox
import subprocess

game_quiz = ".\quiz.py"
game_snake = ".\snake.py"
game_tictactoe = ".\tictactoe.py"

class SpieleAuswahlGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Spiele Auswahl")
        self.root.geometry("100x200")

        # Labels und Buttons hinzufügen
        label = tk.Label(root, text="Wähle ein Spiel:")
        label.pack(pady=10)

        button_spiel1 = tk.Button(root, text="Quiz", command=self.spiel1_starten)
        button_spiel1.pack(pady=5)

        button_spiel2 = tk.Button(root, text="TicTacToe", command=self.spiel2_starten)
        button_spiel2.pack(pady=5)

        button_spiel3 = tk.Button(root, text="Snake", command=self.spiel3_starten)
        button_spiel3.pack(pady=5)

      

    def spiel1_starten(self):
        messagebox.showinfo("Quiz", "Quiz wird gestartet.")
        subprocess.run(["python", game_quiz])

    def spiel2_starten(self):
        messagebox.showinfo("TicTacToe", "TicTacToe wird gestartet.")
        subprocess.run(["python", game_snake])

    def spiel3_starten(self):
        messagebox.showinfo("Snake", "Snake wird gestartet.")
        subprocess.run(["python", game_tictactoe])

if __name__ == "__main__":
    root = tk.Tk()
    app = SpieleAuswahlGUI(root)
    root.mainloop()
