**Dieses Dokument beschreibt die Grading Criteria +  wie wir sie umgesetzt haben**


In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

# **FACHKOMPETENZ (40 Punkte)**

### Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen
 Kenntnisse in prozeduraler Programmierung:
 - Algorithmenbeschreibung
 - Datentypen
 - E/A-Operationen und Dateiverarbeitung
 - Operatoren
 - Kontrollstrukturen
 - Funktionen
 - Stringverarbeitung

[Codezeilen sind zu finden hier](https://github.com/JamesCodingSpace/mgLauncher/blob/main/Launcher/Games/tictactoe/tictactoe.py)

**Algorithmenbeschreibung:**
Der Code implementiert das Spiel "Tic Tac Toe" mit einer einfachen KI für den Einzelspielermodus.
Die KI verwendet den Minimax-Algorithmus, um den besten Zug für den Computer zu berechnen.
Es gibt Funktionen, um den Gewinner zu überprüfen, einen Zug zu machen, das Spiel neu zu starten und den Spielmodus zu wählen.

```
def minimax(board, maximizing):
    if check_winner(board, "X"):
        return -1
    elif check_winner(board, "O"):
        return 1
    elif check_draw(board):
        return 0

    if maximizing:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score
```


**Datentypen:**
Der Code verwendet Listen für das Spielfeld (board), Strings für die Symbole ("X" und "O"), Tupel für die Positionen und Booleans für den Spielzustand.

```
# Beispiel: Liste für das Spielfeld
board = [[" " for _ in range(3)] for _ in range(3)]

# Beispiel: Strings für Symbole
current_player = "X"

# Beispiel: Tupel für Positionen
text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))

# Beispiel: Booleans für Spielzustand
game_over = False
```

**E/A-Operationen und Dateiverarbeitung:**
Das Spiel verwendet Pygame für Ein-/Ausgabeoperationen und die Darstellung auf dem Bildschirm.
Es gibt jedoch keine Dateiverarbeitung im Code.

```
# Pygame wird für Ein-/Ausgabeoperationen und Darstellung verwendet
import pygame

# Beispiel: Anzeige auf dem Bildschirm
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
```

**Operatoren:**
Der Code verwendet grundlegende arithmetische Operatoren wie Addition, Division und Modulo, um die Positionen auf dem Spielfeld zu berechnen.
Es gibt auch Vergleichsoperatoren wie Gleichheit und Ungleichheit für die Überprüfung von Bedingungen.

```
# Beispiel: Arithmetische Operatoren für Berechnungen
CELL_SIZE = WIDTH // 3

# Beispiel: Vergleichsoperatoren für Bedingungsüberprüfung
if event.type == pygame.MOUSEBUTTONDOWN and not game_over and current_player == "X":
```

**Kontrollstrukturen:**
Der Code verwendet Schleifen wie for-Schleifen, um über das Spielfeld zu iterieren und den besten Zug für die KI zu finden.
Es gibt if, elif und else-Anweisungen für die Bedingungsüberprüfung und Steuerung des Spielablaufs.

```
# Beispiel: for-Schleifen für Iterationen
for i in range(3):
    for j in range(3):
        if board[i][j] == " ":
```

**Funktionen:**
Der Code definiert mehrere Funktionen für verschiedene Aspekte des Spiels, wie das Zeichnen des Spielfelds, Überprüfen des Gewinners, das Treffen von Zügen und das Wählen des Spielmodus.

```
# Beispiel: Funktionsdefinition für das Zeichnen des Spielfelds
def draw_board():
    WIN.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(WIN, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 3)
    # ...
```

**Stringverarbeitung:**
Die Pygame-Bibliothek wird verwendet, um Text auf dem Bildschirm darzustellen, wie die Anzeige des Gewinners und der Optionen im Menü.
Die Verarbeitung von Zeichenketten ist jedoch nicht der Schwerpunkt des Codes, da die meiste Logik auf Listen und Symbolen basiert.

```
# Beispiel: Verwendung von Pygame, um Text anzuzeigen
font = pygame.font.SysFont(None, 50)
text = font.render("It's a draw!", True, BLACK)

```

### Sie können die Syntax und Semantik von Python (10)
Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen

[Codezeilen sind zu finden hier](https://github.com/JamesCodingSpace/mgLauncher/blob/main/Launcher/Games/snake/snake.py)

```
for y in range(dis_height):
            for x in range(dis_width):
                if (x + y) % 2 == 0:
                    color = green
                else:
                    color = green2
                pygame.draw.rect(dis, color, (x * snake_block, y * snake_block, snake_block, snake_block))
```

**Effiziente Darstellung von Schachbrettmustern:** 
Durch die Verwendung von Schleifen wird das Schachbrettmuster effizient generiert, da für jedes Feld im Raster überprüft wird, ob die Summe der x- und y-Koordinaten gerade ist oder nicht. Dadurch entsteht das charakteristische Schachbrettmuster mit abwechselnden Farben.

**Kompakte und elegante Implementierung:**
Der Code ist kurz und prägnant, was auf eine gute Kenntnis der Python-Sprache und ihrer Funktionen hindeutet. Durch die Verwendung einer einfachen Bedingung innerhalb einer doppelten Schleife wird das Schachbrettmuster erstellt, ohne unnötige Komplexität einzuführen.

**Lesbarkeit und Verständlichkeit:** 
Der Code ist gut strukturiert und leicht verständlich. Durch die Verwendung aussagekräftiger Variablennamen wie "green" und "green2" ist klar, was der Zweck der Farben ist, und die Bedingung (x + y) % 2 == 0 ist intuitiv verständlich, um gerade und ungerade Felder zu unterscheiden.

**Flexibilität und Anpassbarkeit:** 
Durch die Verwendung von Variablen wie "dis_height", "dis_width" und "snake_block" kann das Schachbrettmuster leicht an verschiedene Größen und Einstellungen angepasst werden. Dies zeigt eine gute Planung und Flexibilität bei der Implementierung.

**Visuelle Ästhetik:** 
Das generierte Schachbrettmuster ist visuell ansprechend und gut gestaltet. Die klare Unterscheidung zwischen den beiden Farben und die gleichmäßige Verteilung auf dem Bildschirm tragen dazu bei, dass das Ergebnis professionell aussieht.



### Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat

**WICHTIG**
Sämtliche Commits wurde aufgrund von Problemen bei der Verknüpfung von GitHub und VSC über einen Account hochgeladen.
Die Owner der einzelnen Programme haben diese aber in den gleichnamigen Discussions erklärt.
Somit können sie nachverfolgen, wer was am Projekt gemacht hat.

### Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen

[Codezeilen sind zu finden hier](https://github.com/JamesCodingSpace/mgLauncher/blob/main/Launcher/Games/quiz/quiz.py)

```
def start_quiz(self):
    random.shuffle(questions)
    self.score = 0
    self.current_question_index = 0
    self.show_question()
```
**Liste:** 
Die Liste questions enthält eine Sammlung von Fragen und Antworten in Form von Wörterbucheinträgen.

**Dictionary:** 
Jeder Eintrag in der Liste questions ist ein Wörterbucheintrag mit einem Frage-Schlüssel und einem Antwort-Schlüssel.

**Strings:** 
Die Fragen und Antworten werden als Zeichenketten innerhalb der Wörterbuch-Einträge gespeichert.


# METHODENKOMPETENZ (10 Punkte)

### Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein

GitHub wurde verwendet siehe [hier](https://github.com/JamesCodingSpace/mgLauncher) 

VSC wurde von jedem Gruppenmitglied als Umgebung verwendet 
![image](https://github.com/JamesCodingSpace/mgLauncher/assets/152854421/dc6e69ae-fef6-440b-8a42-cc53abd8ebaf)


# PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

### Die Studierenden können ihre Software erläutern und begründen. (5)
Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person)
![image](https://github.com/JamesCodingSpace/mgLauncher/assets/152854421/ada96ed9-cbfe-4aa8-b5c9-415faf1e8e34)
![image](https://github.com/JamesCodingSpace/mgLauncher/assets/152854421/53d80953-b984-4d44-adf5-a7b6645cd93b)
![image](https://github.com/JamesCodingSpace/mgLauncher/assets/152854421/c845cb00-46be-42c5-9e2f-290bbc58846c)
![image](https://github.com/JamesCodingSpace/mgLauncher/assets/152854421/eeefc07f-0d95-4f60-a804-75f5a21be06a)


### Sie können existierenden Code analysieren und beurteilen. (5)
Pro Gruppe: You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes

Zu sehen in der Review-GradingCriteria.md

### Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
**Which technology did you learn outside of the teacher given input**

- Tkinter
- PyGame

Did you or your group get help from someone in the classroom (get a support message here from the person who helped you)

Dominik Neubauer helped us with setting up a PyGame enviorment and gone through the process of troubleshooting and bugfixing after finishing out project.

![Screenshot 2024-02-26 164534](https://github.com/JamesCodingSpace/mgLauncher/assets/152854421/685a242a-bcc4-4e65-8408-407955f14ff9)


# ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

### Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
*Which parts of your project are you proud of and why (describe, analyse, link)*

**Strukturierte Implementierung des Spiele:** 
Die Struktur des Codes ist klar und organisiert. Die verschiedenen Funktionen sind gut definiert und tragen jeweils zu einem bestimmten Aspekt der Spielimplementierung bei, was die Wartbarkeit und Lesbarkeit unseres Codes verbessert hat.

**Einsatz des Minimax-Algorithmus im Spiel TicTacToe:** 
Die Implementierung des Minimax-Algorithmus für die KI im Einzelspielermodus ist ein wichtiger Teil des Codes. Die Fähigkeit, eine KI zu entwickeln, die gegen den Spieler spielt und gute Entscheidungen trifft, ist für uns ein beachtlicher Erfolg.
Natürlich ist diese KI noch lange nicht perfekt, hierfür hat dann aber auch einfach die Zeit nicht gereicht.

**Verwendung von Pygame für die Grafikdarstellung:** 
Die Integration von Pygame zur Darstellung der grafischen Benutzeroberfläche des Spieler war ein großes Ziel für uns.
Die Verwendung von Grafiken und Benutzeroberflächenelementen trägt wesentlich zur Benutzererfahrung bei und lassen die Spiele professioneller wirken.

**Interaktiver Spielmodus:** 
Die Implementierung eines interaktiven Spielmodus, in dem der Benutzer zwischen Einzelspieler- und Mehrspielermodus wählen kann, erweitert die Funktionalität des Spiels TicTacToe und macht es vielseitiger und ansprechender.

**Gewinnererkennung und Spiellogik:** 
Die korrekte Erkennung des Gewinners und die Überprüfung auf Unentschieden im Spiel TicTacToe, sowie die Erkennung von Kollisionen der Schlange, aber auch der Tetris Tiles sind wesentlicher Bestandteil der Spiele. 
Die Logik hinter diesen Funktionen zeigt ein tiefes Verständnis des Spielablaufs und beweisen, dass wir neue Methoden kennen gelernt haben, sowie diese eingesetzt haben.

*Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant)*

Wir als Gruppe hatten ein paar Probleme während des Projektablaufs:

- Zeitmanagment
Die von uns gesetzten Ziele konnte in der kurzen Zeitspanne von 2 Wochen nicht wirklich alle umgesetzt werden, was darauf hinaus lief, dass wir als Gruppe vor allem vor der Präsentation in der Klasse sehr lange Nächte hatten.
Hier müssen wir aber auch dazu sagen, dass vor allem für Anfänger, welche ja ebenfalls ein gutes Projekt abliefern möchten, die Zeit vollkommen unzureichend gewesen ist.

- Funktionalität 
Die Funktionalität unseres Projektes ist gegeben. Gefundene Bugs wurden zum Großteil behoben, jedoch kann man auch hier in der kurzen Zeit nicht wirklich ein perfektes Ergebnis abliefern.
Die verfügbare Zeit musste abgewogen werden und Dokumentation und die Bewertung anderer Gruppen haben viel zu viel Zeit gefressen, sodass bei der Funktionalität teils Kompromisse eingegangen werden mussten.
Ebenfalls waren große Wiedersprüche im laufe des Semesters bezüglich Anforderungen und Ziele der Abgabe vorhanden.

- Team Management
Unser Team bestand aus drei sich noch relativ unbekannten Studenten.
Die Idee für unser Projekt war sowohl einsteigerfreundlich, als auch gut für fortgeschrittene Programmierer.
Es hat sich als Lebensretten erwiesen, dass einer der Gruppe bereits langjährige Python Erfahrungen mit sich gebracht hat.
Falls die Gruppe aus drei vollkommenen Anfängern bestanden hätte, vermuten wir, dass das Projekt vollkommen gescheitert wäre,
da die Anfänger im Kurs vollkommen vernachlässigt wurden.

# Fazit (offtopic)
Die Intention des Kurses ist mir immer noch unbekannt.
War er da um neuen Informatikern einen Einstieg in die Welt der Programmierung zu geben, oder einfach nur dafür da, dass Studenten mit Erfahrung einen Lehrauftrag bekommen haben.
Einen Großteil der Bewertung darauf auszulegen, anderen zu helfen und andere zu bewerten ist einfach unsinnig für Anfänger, da diese meist gar nicht helfen können und erst recht nicht in komplexen Programmen anderer irgendetwas kritisieren können.
Daraus 20% der Note zu machen ist meiner Meinung nach einfach nur unfair und diskriminiert die Anfänger total.

Der Kurs bestand für die meisten nicht darin das Programmieren zu erlernen, sondern sich damit zu beschäftigen, was genau jetzt die Anforderungen der Abgaben sind, da diese nicht wirklich verständlich gemacht worden sind.
Ebenfalls ist die Zeitspanne von 2 Wochen viel zu wenig, vor allem erneut für Anfänger, ein ordentliches Projekt ab zu geben, da alleine die Dokumentation viel zu lange gedauert hat.

Ich, Jamie Rohner, empfand den Kurs als Zeitverschwendung und bezweifle ganz stark, dass die Anfänger der Python Programmierung überhaupt irgendeinen Mehrwert aus diesem Semester Programmieren hatten, sofern sie sich nicht wirklich alles selbst beigebracht haben.


