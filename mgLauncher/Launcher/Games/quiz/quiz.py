import tkinter as tk
from tkinter import messagebox
import random
import time

questions = [
    {"question": "Wie lautet die Hauptstadt von Frankreich?", "answer": "Paris"},
    {"question": "Wie viele Planeten hat unser Sonnensystem?", "answer": "8"},
    {"question": "Wer ist der aktuelle Bundeskanzler?", "answer": "Olaf Scholz"},
    {"question": "In welchem Land liegt der Berg Kilimandscharo?", "answer": "Tansania"},
    {"question": "Zu welcher Elementgruppe gehört das Element Radon?", "answer": "Edelgase"},
    {"question": "Welches ist das größte Säugetier der Welt?", "answer": "Blauwal"},
    {"question": "Wer hat die Relativitätstheorie entwickelt?", "answer": "Albert Einstein"},
    {"question": "Wie viele Kontinente gibt es?", "answer": "7"},
    {"question": "Welches ist das längste Fluss der Welt?", "answer": "Nil"},
    {"question": "Welches ist das kleinste Land der Welt?", "answer": "Vatikanstadt"},
    {"question": "Wie viele Ozeane gibt es?", "answer": "3"},
    {"question": "Wie nennt man die kleinste Einheit eines Elements?", "answer": "Atom"},
    {"question": "Wer ist der berühmteste Detektiv der Weltliteratur?", "answer": "Sherlock Holmes"},
    {"question": "Wie viele Spieler hat eine Fußballmannschaft auf dem Feld?", "answer": "11"},
    {"question": "Welches ist das häufigste chemische Element in der Erdkruste?", "answer": "Sauerstoff"},
    {"question": "Welcher Planet ist der dritte von der Sonne aus?", "answer": "Erde"},
    {"question": "Wie viele Sekunden hat ein Tag?", "answer": "86400"},
    {"question": "Wie nennt man die kleinste Blutgefäßart im menschlichen Körper?", "answer": "Kapillare"},
    {"question": "Wie nennt man die Wissenschaft von den Lebewesen?", "answer": "Biologie"},
    {"question": "Wie lautet die chemische Formel für Wasser?", "answer": "H2O"},
]

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz")
        self.geometry("400x200")
        
        self.label = tk.Label(self, text="Willkommen zum Quiz!")
        self.label.pack()
        
        self.button = tk.Button(self, text="Start Quiz", command=self.start_quiz)
        self.button.pack()
        
    def start_quiz(self):
        random.shuffle(questions)
        self.score = 0
        self.current_question_index = 0
        self.show_question()

    def show_question(self):
        if self.current_question_index < len(questions):
            self.question_data = questions[self.current_question_index]
            self.question_label = tk.Label(self, text=self.question_data["question"])
            self.question_label.pack()
            self.entry = tk.Entry(self)
            self.entry.pack()
            self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
            self.submit_button.pack()
            self.start_time = time.time()
        else:
            messagebox.showinfo("Quiz beendet", f"Quiz beendet! Du hast {self.score} von {len(questions)} Fragen richtig beantwortet.")

    def check_answer(self):
        user_answer = self.entry.get()
        correct_answer = self.question_data["answer"]
        elapsed_time = time.time() - self.start_time

        if elapsed_time > 30:
            messagebox.showinfo("Zeit abgelaufen", f"Zeit abgelaufen! Die richtige Antwort ist: {correct_answer}")
        elif user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Richtig", "Richtig!")
            self.score += 1
        else:
            messagebox.showinfo("Falsch", f"Falsch! Die richtige Antwort ist: {correct_answer}")

        self.current_question_index += 1
        self.clear_question_widgets()
        self.show_question()

    def clear_question_widgets(self):
        self.question_label.pack_forget()
        self.entry.pack_forget()
        self.submit_button.pack_forget()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
