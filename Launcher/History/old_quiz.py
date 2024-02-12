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
    {"question": "Wie viele Sekunden hat ein Tag?", "answer": "1440"},
    {"question": "Wie nennt man die kleinste Blutgefäßart im menschlichen Körper?", "answer": "Kapillare"},
    {"question": "Wie nennt man die Wissenschaft von den Lebewesen?", "answer": "Biologie"},
    {"question": "Wie lautet die chemische Formel für Wasser?", "answer": "H2O"},
]

import random
import time

def run_quiz(questions, time_limit_per_question=30):
    score = 0
    random.shuffle(questions)

    for question_data in questions:
        question = question_data["question"]
        correct_answer = question_data["answer"]

        print(question)
        start_time = time.time()
        
        user_answer = input(f"")

        elapsed_time = time.time() - start_time

        if elapsed_time > time_limit_per_question:
           print(f"Zeit abgelaufen! Die richtige Antwort ist: {correct_answer}")
        elif user_answer.lower() == correct_answer.lower():
            print("Richtig!")
            score += 1
        else:
            print(f"Falsch! Die richtige Antwort ist: {correct_answer}")

    print(f"\nQuiz beendet! Du hast {score} von {len(questions)} Fragen richtig beantwortet.")

    if score >= 15:
        print("Glückwunsch! Das ist ein sehr gutes Ergebnis!")

def start_quiz():
    ready = input("Wenn du bereit bist, schreibe 'bereit' und drücke Enter! ")
    if ready.lower() == "bereit":
        run_quiz(questions)

print("Willkommen zum Quiz! Du hast für jede Frage 30 Sekunden Zeit zu antworten, ansonsten zählt die Antwort automatisch als falsch! Hinweis: Gebe bei Fragen nach einer Zahl als Antwort die Zahl und nicht das Zahlenwort.")

start_quiz()

